from fastapi import APIRouter, UploadFile
import shutil
import os

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile):
    file_location = f"data/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": f"File saved at {file_location}"}