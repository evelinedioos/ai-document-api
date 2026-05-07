from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

from pydantic import BaseModel


class TextInput(BaseModel):
    text: str


@app.post("/summarize")
def summarize(input: TextInput):
    return {
        "summary": f"Summary of: {input.text}"
    }