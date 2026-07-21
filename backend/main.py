from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile, File
from pdf_service import extract_text_from_pdf
from chunk_service import split_text
from embeding_service import create_embeddings
from vector_store import store_chunks
from rag_service import ask_question

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

    # Step 1: Extract PDF text
    text = extract_text_from_pdf(file.file)

    # Step 2: Split text into chunks
    chunks = split_text(text)

    # Step 3: Create embeddings
    embeddings = create_embeddings(chunks)

    # Step 4: Store chunks + embeddings
    total_stored = store_chunks(
        chunks,
        embeddings
    )

    return {
        "filename": file.filename,
        "total_chunks": len(chunks),
        "stored_chunks": total_stored,
        "message": "PDF processed and stored successfully"
    }

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(request: QuestionRequest):

    result = ask_question(
        request.question
    )

    return result