from app.utils.references import format_references
from app.core.retriever import retrieve_relevant_chunks
from app.core.llm import get_llm
from app.core.prompts import QA_PROMPT_TEMPLATE


def answer_question(question: str):
    """
    RAG-based question answering with justification
    """
    retrieved_chunks = retrieve_relevant_chunks(question,top_k=6)

    context = "\n\n".join(
        [chunk["text"] for chunk in retrieved_chunks]
    )

    llm = get_llm()

    prompt = QA_PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    response = llm.invoke(prompt)

    return {
    "answer": response.content,
    "references": format_references(
        [chunk["metadata"] for chunk in retrieved_chunks]
    )
}
