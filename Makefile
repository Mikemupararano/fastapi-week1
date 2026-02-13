run-root:
python -m uvicorn main:app --reload --port 8000

run-week1:
cd week1-fastapi && python -m uvicorn main:app --reload --port 8001

run-week2:
cd week2-fastapi && python -m uvicorn main:app --reload --port 8002
