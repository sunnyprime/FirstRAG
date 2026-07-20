from fastapi import FastAPI
from pydantic import BaseModel

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