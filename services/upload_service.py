from fastapi import UploadFile
from services.pdf_service import extract_text_from_pdf

async def process_upload(file: UploadFile):

    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "text_preview": text[:500]
        }

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Only PDF processing is supported right now"
    }