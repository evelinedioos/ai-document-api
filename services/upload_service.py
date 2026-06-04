import uuid #uuid kan unieke ID's maken.

from fastapi import UploadFile, HTTPException
from services.pdf_service import extract_text_from_pdf, get_pdf_page_count
from services.summarize_service import generate_summary
from data.document_store import documents


async def process_upload(file: UploadFile):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

    try:
        page_count = get_pdf_page_count(file)

        file.file.seek(0)
        text = extract_text_from_pdf(file)

        document_id = str(uuid.uuid4())
        documents[document_id] = text

        summary = generate_summary(text)

        return {
            "document_id": document_id,
            "filename": file.filename,
            "content_type": file.content_type,
            "page_count": page_count,
            "character_count": len(text),
            "text_preview": text[:500],
            "summary": summary
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while processing the PDF"
        )