from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def root():
    return {"message": "API running"}

class TextInput(BaseModel):
    text: str


@app.post("/summarize")
def summarize(input: TextInput):
    return {
        "summary": f"Summary of: {input.text}"
    }
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }