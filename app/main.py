from fastapi import FastAPI
from app.models.user import UserCreate

app = FastAPI(title="FastAPI Week 1")


@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}


@app.post("/users")
def create_user(user: UserCreate):
    return {"created": True, "user": user}
