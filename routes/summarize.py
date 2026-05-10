from fastapi import APIRouter
from pydantic import BaseModel
from services.summarize_service import generate_summary

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/summarize")
def summarize(input: TextInput):
    summary = generate_summary(input.text)

    return {
        "summary": summary
    }