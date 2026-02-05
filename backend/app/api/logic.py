from fastapi import APIRouter
from app.services.logic_service import (
    generate_logic_question,
    evaluate_user_answer
)
from app.models.schemas import (
    LogicQuestionResponse,
    LogicEvaluationRequest,
    LogicEvaluationResponse
)

router = APIRouter()


@router.get("/logic/question", response_model=LogicQuestionResponse)
def get_logic_question():
    return generate_logic_question()


@router.post("/logic/evaluate", response_model=LogicEvaluationResponse)
def evaluate_answer(request: LogicEvaluationRequest):
    return evaluate_user_answer(
        request.question,
        request.user_answer
    )
