from fastapi import FastAPI
from routes.summarize import router as summarize_router
from routes.upload import router as upload_router
from utils.config import APP_NAME

app = FastAPI(title=APP_NAME)

app.include_router(summarize_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {"message": "API running"}