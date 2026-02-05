QA_PROMPT_TEMPLATE = """
You are an intelligent research assistant.

Answer the question using the provided document context as the PRIMARY source.
You MAY use outside general knowledge ONLY IF:
- it is relevant to the question, and
- it helps complete or clarify the answer, and
- it does NOT contradict the document context.

Context:
{context}

Question:
{question}

Rules:
- Prefer the document context whenever possible
- Outside knowledge must be accurate and relevant
- Clearly base the answer on the document, even if enriched by general knowledge
- If the question cannot be answered from context or reasonable knowledge, say:
  "Answer not found in the document."
- Provide a clear, concise answer
"""

DOCUMENT_SUMMARY_PROMPT = """
You are a professional research assistant.

Your task is to write a clear, detailed, and easy-to-understand summary of the document content below.

Rules:
- Use SIMPLE English
- Cover ALL important ideas
- Do NOT miss sections
- Do NOT add outside knowledge
- Do NOT hallucinate
- Write in paragraph form
- The summary should be LONG and informative, not short

Document Content:
{content}

Now write a well-structured, detailed summary:
"""
