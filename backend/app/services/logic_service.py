from app.utils.references import format_references
from app.core.retriever import retrieve_relevant_chunks
from app.core.llm import get_llm


def generate_logic_question():
    """
    Generate a logic/comprehension-based question
    from the document content.
    """
    chunks = retrieve_relevant_chunks(
        "key objective or main idea of the document",
        top_k=3
    )

    context = "\n\n".join(chunk["text"] for chunk in chunks)

    llm = get_llm()

    prompt = f"""
You are a tutor.

Based ONLY on the following document context,
generate ONE logic-based comprehension question.

Context:
{context}

Rules:
- Question must require understanding, not copying
- Do NOT include the answer
"""

    response = llm.invoke(prompt)

    return {
    "question": response.content.strip(),
    "references": format_references(
        [chunk["metadata"] for chunk in chunks]
    )
}





def evaluate_user_answer(question: str, user_answer: str):
    """
    Evaluate user's answer against document context.
    """
    chunks = retrieve_relevant_chunks(question, top_k=4)

    context = "\n\n".join(chunk["text"] for chunk in chunks)

    llm = get_llm()

    prompt = f"""
You are an evaluator.

Evaluate the user's answer using ONLY the context below.

Context:
{context}

Question:
{question}

User Answer:
{user_answer}

Tasks:
1. Decide if the answer is Correct, Partially Correct, or Incorrect
2. Explain WHY using the document context
"""

    response = llm.invoke(prompt)

    return {
    "evaluation": response.content.strip(),
    "references": format_references(
        [chunk["metadata"] for chunk in chunks]
    )
}
