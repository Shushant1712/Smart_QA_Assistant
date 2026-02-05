from fastapi import APIRouter
from app.core.vectorstore import load_vector_store
from app.services.summary_service import generate_document_summary

router = APIRouter(tags=["Summary"])


@router.post("/summary")
def generate_summary():
    """
    Generate document summary ONLY on user request
    """
    vector_store = load_vector_store()

    # Retrieve representative chunks
    docs = vector_store.similarity_search(
    query=".",
    k=1000  # fetch ALL chunks
)

    chunks = [doc.page_content for doc in docs]

    summary = generate_document_summary(chunks)

    return {
        "summary": summary
    }
