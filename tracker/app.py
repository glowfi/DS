from flask import Flask
from models import db
import os
from flask import render_template, request, redirect, url_for, jsonify, flash, send_file
from models import db, Topic, Question
from utils import questions_to_json_rows, import_data
import io, csv, json, pandas as pd

app = Flask(__name__)
app.secret_key = "dev-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dsa_tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    topics = Topic.query.order_by(Topic.sort_index).all()

    topics_with_q = []
    total_left = 0  # ← global “left” counter
    for t in topics:
        qs = Question.query.filter_by(topic_id=t.id).order_by(Question.sort_index).all()
        total = len(qs)
        completed = sum(1 for q in qs if q.completed)
        total_left += total - completed  # add this topic’s remaining

        topics_with_q.append((t, qs, completed, total))

    total_questions = Question.query.count()

    return render_template(
        "index.html",
        topics_with_q=topics_with_q,
        total_questions=total_questions,
        global_left=total_left,  # pass to the template
    )


@app.route("/topic/add", methods=["POST"])
def add_topic():
    name = request.form.get("name", "").strip()
    if not name:
        flash("Topic name cannot be empty", "danger")
        return redirect(url_for("index"))
    last = db.session.query(db.func.max(Topic.sort_index)).scalar() or 0
    db.session.add(Topic(name=name, sort_index=last + 1))
    db.session.commit()
    flash("Topic added", "success")
    return redirect(url_for("index"))


@app.route("/question/add", methods=["POST"])
def add_question():
    topic_id = request.form.get("topic_id")
    problem = request.form.get("problem", "").strip()
    pattern = request.form.get("pattern", "").strip()
    question_link = request.form.get("link", "").strip()
    if not topic_id or not problem:
        flash("Topic and Problem required", "danger")
        return redirect(url_for("index"))
    qs = (
        Question.query.filter_by(topic_id=int(topic_id))
        .order_by(Question.sort_index)
        .all()
    )
    sort_index = qs.pop(-1).sort_index + 1 if len(qs) > 0 else 0
    db.session.add(
        Question(
            topic_id=int(topic_id),
            problem=problem,
            pattern=pattern,
            question_link=question_link,
            sort_index=sort_index,
        )
    )
    db.session.commit()
    flash("Question added", "success")
    return redirect(url_for("index"))


@app.route("/question/edit/<int:q_id>", methods=["POST"])
def edit_question(q_id):
    q = Question.query.get_or_404(q_id)
    problem = request.form.get("problem", "").strip()
    pattern = request.form.get("pattern", "").strip()
    question_link = request.form.get("link", "").strip()
    if not problem:
        return jsonify({"ok": False, "error": "Problem cannot be empty"}), 400
    q.problem = problem
    q.pattern = pattern
    q.question_link = question_link
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/question/delete/<int:q_id>", methods=["POST"])
def delete_question(q_id):
    q = Question.query.get_or_404(q_id)
    db.session.delete(q)
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/question/toggle/<int:q_id>", methods=["POST"])
def toggle_question(q_id):
    q = Question.query.get_or_404(q_id)
    q.completed = not q.completed
    db.session.commit()
    return jsonify({"ok": True, "completed": q.completed})


@app.route("/questions/reorder/<int:topic_id>", methods=["POST"])
def reorder_questions(topic_id):
    """
    Expects JSON: [question_id_1, question_id_2, ...] in the new order.
    The order is saved in the ``sort_index`` column of Question.
    """
    # Ensure the topic exists
    topic = Topic.query.get_or_404(topic_id)

    order = request.get_json(silent=True)
    if not isinstance(order, list):
        return jsonify({"ok": False, "error": "Invalid payload"}), 400

    for idx, qid in enumerate(order):
        q = Question.query.filter_by(id=int(qid), topic_id=topic.id).first()
        if q:
            q.sort_index = idx  # store the new position
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/topics/reorder", methods=["POST"])
def reorder_topics():
    order = request.get_json(silent=True)
    if not isinstance(order, list):
        return jsonify({"ok": False, "error": "Invalid payload"}), 400

    for idx, tid in enumerate(order):
        topic = Topic.query.get(int(tid))
        if topic:
            topic.sort_index = idx
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/export/<fmt>")
def export(fmt):
    rows = questions_to_json_rows()
    if fmt == "json":
        # Serialize to JSON and write to a BytesIO buffer
        json_bytes = json.dumps(rows, indent=2).encode("utf-8")
        buffer = io.BytesIO(json_bytes)

        # Reset pointer to the start of the buffer
        buffer.seek(0)

        return send_file(
            buffer,
            as_attachment=True,
            download_name="questions.json",
            mimetype="application/json",
        )
    elif fmt == "csv":
        si = io.StringIO()
        writer = csv.DictWriter(si, fieldnames=rows[0].keys())
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
        return send_file(
            io.BytesIO(si.getvalue().encode()),
            as_attachment=True,
            download_name="questions.csv",
        )
    elif fmt == "excel":
        df = pd.DataFrame(rows)
        mem = io.BytesIO()
        with pd.ExcelWriter(mem, engine="openpyxl") as writer:
            df.to_excel(writer, index=False)
        mem.seek(0)
        return send_file(mem, as_attachment=True, download_name="questions.xlsx")
    return "Invalid format", 400


@app.route("/import", methods=["POST"])
def import_file():
    f = request.files.get("file")
    if not f:
        flash("No file uploaded", "danger")
        return redirect(url_for("index"))
    try:
        db.session.execute(Topic.__table__.delete())
        db.session.execute(Question.__table__.delete())
        db.session.commit()
        import_data(f)
        flash("Imported successfully", "success")
    except Exception as e:
        flash("Import failed: " + str(e), "danger")
    return redirect(url_for("index"))


@app.route("/topics/delete_batch", methods=["POST"])
def delete_topics_batch():
    ids = request.get_json(silent=True)
    if not isinstance(ids, list):
        return jsonify({"ok": False, "error": "Invalid payload"}), 400
    for tid in ids:
        topic = Topic.query.get(int(tid))
        if topic:
            # Automatically cascades to delete questions if you have `backref` set
            db.session.delete(topic)
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/questions/delete_batch", methods=["POST"])
def delete_questions_batch():
    ids = request.get_json(silent=True)
    if not isinstance(ids, list):
        return jsonify({"ok": False, "error": "Invalid payload"}), 400
    for qid in ids:
        q = Question.query.get(int(qid))
        if q:
            db.session.delete(q)
    db.session.commit()
    return jsonify({"ok": True})


@app.route("/questions/move", methods=["POST"])
def move_questions():
    data = request.get_json(silent=True)
    q_ids = data.get("question_ids", [])
    target_topic_id = data.get("target_topic_id")

    if not isinstance(q_ids, list) or not target_topic_id:
        return jsonify({"ok": False, "error": "Invalid payload"}), 400

    target_topic = Topic.query.get(target_topic_id)
    if not target_topic:
        return jsonify({"ok": False, "error": "Target topic not found"}), 404

    # Get the last sort_index in target topic
    last_sort_index = (
        db.session.query(db.func.max(Question.sort_index))
        .filter_by(topic_id=target_topic.id)
        .scalar()
        or 0
    )

    for i, qid in enumerate(q_ids):
        q = Question.query.get(int(qid))
        if q:
            q.topic_id = target_topic.id
            q.sort_index = last_sort_index + i + 1

    db.session.commit()
    return jsonify({"ok": True})


@app.route("/topic/rename/<int:topic_id>", methods=["POST"])
def rename_topic(topic_id):
    """Rename a topic – called via AJAX from the modal."""
    topic = Topic.query.get_or_404(topic_id)
    new_name = request.form.get("name", "").strip()
    if not new_name:
        return jsonify({"ok": False, "error": "Name cannot be empty"}), 400

    exists = Topic.query.filter(Topic.id != topic_id, Topic.name == new_name).first()
    if exists:
        return (
            jsonify({"ok": False, "error": "Another topic already uses that name"}),
            400,
        )

    topic.name = new_name
    db.session.commit()
    return jsonify({"ok": True, "name": new_name})


if __name__ == "__main__":
    from utils import init_db

    with app.app_context():
        init_db()
    app.run(debug=True)
