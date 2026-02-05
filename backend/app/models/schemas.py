from pydantic import BaseModel
from typing import List, Dict, Any


# ---------- Upload ----------

class UploadResponse(BaseModel):
    filename: str
    status: str
    extracted_chunks: int


# ---------- Question Answering ----------

class QuestionRequest(BaseModel):
    question: str


class QAResponse(BaseModel):
    answer: str
    references: List[Dict[str, Any]]


# ---------- Logic ----------

class LogicQuestionResponse(BaseModel):
    question: str
    references: List[Dict[str, Any]]


class LogicEvaluationRequest(BaseModel):
    question: str
    user_answer: str


class LogicEvaluationResponse(BaseModel):
    evaluation: str
    references: List[Dict[str, Any]]
