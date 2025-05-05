from fastapi import APIRouter, Form
from services.gemini import generate_query_code

router = APIRouter()


'''
TODO: 
stub
'''
@router.post("/")
async def process_query(query: str = Form(...), filename: str = Form(...)):
    result = generate_query_code(query, filename)
    return {"result": result}