from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from database.database import get_db
from domain.answer import answer_schema as sc
from domain.answer.answer_crud import *
from domain.question.question_crud import get_question


answer_router = APIRouter(
    prefix='/answer'
)

@answer_router.post('/create/{question_id}', status_code=status.HTTP_204_NO_CONTENT)
def answer_create(question_id : int, _answer_create : sc.AnswerCreate, db:Session=Depends(get_db)):

    question = get_question(db,question_id)
    if not question:
        raise HTTPException(status_code=404, detail='question is not found')
    create_answer(db, question, _answer_create)