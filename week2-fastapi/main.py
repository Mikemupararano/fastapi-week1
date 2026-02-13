from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.routers.health import router as health_router

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "week2-fastapi"),
    version="1.0.0",
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Week 2 FastAPI app running 🚀"}
