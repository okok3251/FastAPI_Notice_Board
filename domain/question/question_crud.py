from database.models import Question
from datetime import datetime


def get_question_list(db):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list


def get_question(db, question_id):
    question = db.query(Question).get(question_id)
    return question


def create_question(db, question):
    db_question = Question(
        subject = question.subject,
        content = question.content,
        create_date = datetime.now()
    )
    db.add(db_question)
    db.commit()
