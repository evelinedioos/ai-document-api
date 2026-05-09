from fastapi import FastAPI, UploadFile, File
from routes.summarize import router as summarize_router

app = FastAPI()

app.include_router(summarize_router)

@app.get("/")
def root():
    return {"message": "API running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type
    }