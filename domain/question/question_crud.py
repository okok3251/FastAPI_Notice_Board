from database.models import Question



def get_question_list(db):
    question_list = db.query(Question)\
        .order_by(Question.create_date.desc())\
        .all()
    return question_list


def get_question(db, question_id):
    question = db.query(Question).get(question_id)
    return question