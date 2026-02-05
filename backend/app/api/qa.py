from fastapi import APIRouter
from app.services.qa_service import answer_question
from app.models.schemas import QuestionRequest, QAResponse

router = APIRouter()


@router.post("/qa", response_model=QAResponse)
def ask_question(request: QuestionRequest):
    return answer_question(request.question)
