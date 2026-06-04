import uuid

from fastapi import UploadFile, HTTPException
from services.pdf_service import extract_text_from_pdf, get_pdf_page_count
from services.summarize_service import generate_summary
from services.chunking_service import create_chunks
from services.openai_service import generate_embedding
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

        chunks = create_chunks(text)

        chunk_data = []

        for chunk in chunks:
            embedding = generate_embedding(chunk)

            chunk_data.append({
                "text": chunk,
                "embedding": embedding
            })

        document_id = str(uuid.uuid4())

        documents[document_id] = {
            "filename": file.filename,
            "text": text,
            "chunks": chunk_data
        }

        summary = generate_summary(text)

        return {
            "document_id": document_id,
            "filename": file.filename,
            "content_type": file.content_type,
            "page_count": page_count,
            "character_count": len(text),
            "chunk_count": len(chunks),
            "text_preview": text[:500],
            "summary": summary
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while processing the PDF"
        )