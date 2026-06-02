from fastapi import UploadFile
from services.pdf_service import extract_text_from_pdf
from services.summarize_service import generate_summary

async def process_upload(file: UploadFile):

    if file.content_type == "application/pdf":
        text = extract_text_from_pdf(file)
        summary = generate_summary(text)

        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "text_preview": text[:500],
            "summary": summary
        }

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Only PDF processing is supported right now"
    }