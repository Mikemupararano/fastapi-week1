from fastapi import FastAPI
from dotenv import load_dotenv
import os
from fastapi.responses import Response

load_dotenv()

app = FastAPI(
    title=os.getenv("APP_NAME", "fastapi-projects"),
    description="Root app for the fastapi-projects monorepo",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "fastapi-projects root API is running 🚀",
        "environment": os.getenv("APP_ENV", "development"),
        "apps": ["week1-fastapi"],
    }


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)
