from fastapi import APIRouter
from domain.question.question_router import question_router
from domain.answer.answer_router import answer_router


combined_router = APIRouter()

combined_router.include_router(question_router) 
combined_router.include_router(answer_router)

