from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File
from pdf_service import extract_text_from_pdf
from chunk_service import split_text

from llm import generate_answer


app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "My first RAG backend is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = generate_answer(request.question)

    return {
        "answer": answer
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file.file)

    chunks = split_text(text)

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "chunks": chunks
    }