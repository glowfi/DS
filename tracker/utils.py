from models import db, Topic, Question
import pandas as pd, json, io, re, os

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "embedded_sheet.md")


def parse_markdown(md_text):
    lines = [l.strip() for l in md_text.strip().splitlines()]
    rows = []
    for l in lines:
        if l.startswith("|") and not re.match(r"^\|\s*-+", l):
            p = [x.strip() for x in l.split("|")[1:-1]]
            if len(p) == 3 and p[0].lower() != "topic":
                rows.append({"topic": p[0], "problem": p[1], "pattern": p[2]})
    return rows


def init_db():
    db.create_all()


def questions_to_json_rows():
    """
    Return a list of dicts representing every question.
    Rows are ordered first by the topic's ``sort_index`` and then by the
    question's ``sort_index`` inside that topic.
    """
    rows = []
    # Order topics by their stored position
    topics = Topic.query.order_by(Topic.sort_index).all()
    c = 1
    for topic in topics:
        # Order questions inside the topic by their stored position
        questions = (
            Question.query.filter_by(topic_id=topic.id)
            .order_by(Question.sort_index)
            .all()
        )
        for q in questions:
            rows.append(
                {
                    "question_no": c,
                    "topic": topic.name,
                    "problem": q.problem,
                    "question_link": q.question_link,
                    "pattern": q.pattern or "",
                    "completed": q.completed,
                }
            )
            c += 1
    return rows


def import_data(file):
    ext = os.path.splitext(file.filename)[1].lower()

    # Load file based on extension
    if ext == ".json":
        rows = json.load(file)
    elif ext == ".csv":
        rows = pd.read_csv(file).to_dict(orient="records")
    else:
        rows = pd.read_excel(file).to_dict(orient="records")

    topic_map = {t.name: t.id for t in Topic.query.all()}
    next_sort_index = len(topic_map)

    for r in rows:
        tname = (r.get("topic") or "").strip()
        prob = (r.get("problem") or "").strip()
        patt = (r.get("pattern") or "").strip()
        link = (r.get("question_link") or r.get("link") or "").strip()
        comp = bool(r.get("completed", False))

        # Skip invalid or empty entries
        if not tname or not prob:
            continue

        # Create topic if new
        if tname not in topic_map:
            t = Topic(name=tname, sort_index=next_sort_index)
            db.session.add(t)
            db.session.flush()  # get t.id without full commit
            topic_map[tname] = t.id
            next_sort_index += 1

        # Add question
        db.session.add(
            Question(
                topic_id=topic_map[tname],
                problem=prob,
                pattern=patt,
                question_link=link,
                completed=comp,
            )
        )

    db.session.commit()
