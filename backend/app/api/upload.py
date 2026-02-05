from fastapi import APIRouter, UploadFile, File
from app.utils.file_utils import validate_file, save_file
from app.services.ingestion_service import ingest_document
from app.models.schemas import UploadResponse

router = APIRouter()

UPLOAD_DIR = "backend/data/documents"


@router.post("/upload", response_model=UploadResponse)
def upload_document(file: UploadFile = File(...)):
    validate_file(file)
    file_path = save_file(file, UPLOAD_DIR)
    extracted_data = ingest_document(file_path)

    return {
        "filename": file.filename,
        "status": "uploaded",
        "extracted_chunks": len(extracted_data)
    }
