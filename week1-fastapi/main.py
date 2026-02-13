from fastapi import FastAPI
from dotenv import load_dotenv
import os
from fastapi.responses import Response
from app.routers.health import router as health_router

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "week1-fastapi"),
    version="1.0.0",
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Week 1 FastAPI app running 🚀"}


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)
