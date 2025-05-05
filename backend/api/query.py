from fastapi import APIRouter, Form
# backend/api/query.py

from fastapi import APIRouter, Form
from services.gemini import generate_query_code
from services.run_query import execute_query_code

router = APIRouter()

@router.post("/")
async def process_query(
    query: str = Form(...),
    filename: str = Form(...),
    mode: str = Form("pandas")  # add "sql" support
):
    code = generate_query_code(query, filename)

    result = execute_query_code(code, filename)

    return {
        "query": query,
        "generated_code": code,
        "result": str(result)
    }
