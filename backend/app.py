
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Workflow Agent Backend Running"}
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend is healthy"}
from pydantic import BaseModel

class ProcessRequest(BaseModel):
    text: str

@app.post("/process")
def process_text(request: ProcessRequest):
    return {"received": request.text, "status": "processed"}


