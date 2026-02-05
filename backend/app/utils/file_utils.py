import os
from fastapi import UploadFile, HTTPException

ALLOWED_EXTENSIONS = {
    ".pdf", ".docx", ".pptx", ".csv", ".xlsx", ".md", ".html", ".txt"
}

MAX_FILE_SIZE_MB = 25


def validate_file(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {ext}"
        )


def save_file(file: UploadFile, upload_dir: str) -> str:
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return file_path
