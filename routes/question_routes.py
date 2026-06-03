from fastapi import APIRouter, UploadFile, File, Form
from services.pdf_service import extract_text_from_pdf
from services.question_service import ask_question

router = APIRouter()


@router.post("/ask")
async def ask_document_question(
    file: UploadFile = File(...),
    question: str = Form(...)
):
    text = extract_text_from_pdf(file)

    answer = ask_question(text, question)

    return {
        "filename": file.filename,
        "question": question,
        "answer": answer
    }