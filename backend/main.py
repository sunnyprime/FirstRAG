from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "My first RAG backend is running"}