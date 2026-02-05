from app.core.prompts import DOCUMENT_SUMMARY_PROMPT
from app.core.llm import get_llm


def generate_document_summary(chunks: list[str]) -> str:
    """
    Generate a detailed summary covering the entire document.
    Uses map-reduce style summarization.
    """
    llm = get_llm()

    # STEP 1: Summarize each chunk (MAP)
    partial_summaries = []

    for chunk in chunks:
        prompt = DOCUMENT_SUMMARY_PROMPT.format(content=chunk)
        response = llm.invoke(prompt)
        partial_summaries.append(response.content)

    # STEP 2: Combine partial summaries (REDUCE)
    combined_summary_text = "\n\n".join(partial_summaries)

    final_prompt = f"""
You are a professional research assistant.

Below are summaries of different parts of a document.

Your task:
- Combine them into ONE coherent summary
- Keep it detailed
- Keep it simple
- Cover the entire document
- Remove repetition
- Maintain logical flow

Partial Summaries:
{combined_summary_text}

Now write the final document summary:
"""

    final_response = llm.invoke(final_prompt)

    return final_response.content
