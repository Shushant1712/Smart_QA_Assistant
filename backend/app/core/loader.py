import os
from fastapi import HTTPException

from app.core.extractors.pdf_extractor import extract_pdf
from app.core.extractors.docx_extractor import extract_docx
from app.core.extractors.pptx_extractor import extract_pptx
from app.core.extractors.csv_extractor import extract_csv
from app.core.extractors.xlsx_extractor import extract_xlsx
from app.core.extractors.md_extractor import extract_md
from app.core.extractors.html_extractor import extract_html


def load_document(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_pdf(file_path)
    elif ext == ".docx":
        return extract_docx(file_path)
    elif ext == ".pptx":
        return extract_pptx(file_path)
    elif ext == ".csv":
        return extract_csv(file_path)
    elif ext == ".xlsx":
        return extract_xlsx(file_path)
    elif ext == ".md":
        return extract_md(file_path)
    elif ext == ".html":
        return extract_html(file_path)

    raise HTTPException(
        status_code=400,
        detail=f"Unsupported file format: {ext}"
    )
