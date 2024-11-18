from datetime import datetime
from database.models import Question, Answer
def create_answer(db,question, _answer_create):
    db_answer = Answer(
        question_id = question.id,
        content = _answer_create.content,
        create_date = datetime.now()
    )
    db.add(db_answer)
    db.commit()