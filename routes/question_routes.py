from fastapi import APIRouter, Form, HTTPException 

from data.document_store import documents
from services.openai_service import generate_embedding, answer_question_about_document
from services.similarity_service import find_most_relevant_chunks

router = APIRouter()


@router.post("/ask/{document_id}")
async def ask_document_question(
    document_id: str,
    question: str = Form(...)
):
    if document_id not in documents:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    document = documents[document_id]

    question_embedding = generate_embedding(question)

    relevant_chunks = find_most_relevant_chunks(
        question_embedding,
        document["chunks"],
        top_k=3
    )

    context = "\n\n".join(
        chunk["text"] for chunk in relevant_chunks
    )

    answer = answer_question_about_document(context, question)

    return {
        "document_id": document_id,
        "question": question,
        "answer": answer,
        "sources_used": len(relevant_chunks),
        "similarities": [
            chunk["similarity"] for chunk in relevant_chunks
        ]
    }