from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.models import Question
from domain.question import question_schema as sc
from domain.question.question_crud import *
from database.database import get_db
from starlette import status


question_router = APIRouter(
    prefix='/question',
)


@question_router.get('/list',response_model=list[sc.Question])
def question_list(db:Session=Depends(get_db)):
    _question_list = get_question_list(db)
    return _question_list

@question_router.get('/detail/{question_id}', response_model=sc.Question)
def question_detail(question_id : int, db:Session=Depends(get_db)):
    question = get_question(db,question_id)
    return question

@question_router.post('/create',status_code=status.HTTP_204_NO_CONTENT)
def question_create(_question : sc.QuestionCreate, db : Session=Depends(get_db)):
    create_question(db,_question)