from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Topic(db.Model):
    __tablename__ = "topic"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    sort_index = db.Column(db.Integer, nullable=False, default=0)

    # Cascade delete all related questions when a topic is deleted
    questions = db.relationship(
        "Question", backref="topic", lazy=True, cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {"id": self.id, "name": self.name, "sort_index": self.sort_index}


class Question(db.Model):
    __tablename__ = "question"

    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
    problem = db.Column(db.String, nullable=False)
    question_link = db.Column(db.String, nullable=True)
    pattern = db.Column(db.String)
    completed = db.Column(db.Boolean, default=False)
    sort_index = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "topic": self.topic.name if self.topic else "",
            "question_link": self.question_link or "",
            "problem": self.problem,
            "pattern": self.pattern,
            "completed": bool(self.completed),
        }
