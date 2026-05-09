from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class TextInput(BaseModel):
    text: str


@router.post("/summarize")
def summarize(input: TextInput):
    return {
        "summary": f"Summary of: {input.text}"
    }