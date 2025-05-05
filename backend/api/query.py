from fastapi import APIRouter, Form
# from services.ai_wrapper import generate_query_code

router = APIRouter()


'''
TODO: 
stub
'''
@router.post("/")
async def process_query(query: str = Form(...), filename: str = Form(...)):
    pass