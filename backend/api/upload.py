from fastapi import APIRouter, UploadFile
import shutil
import os

router = APIRouter()

'''
Directory to save uploaded files
when moving to cloud, change
'''
SAVE_DIR = "./temp"
os.makedirs(SAVE_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile):
    try:
        file_path = os.path.join(SAVE_DIR, file.filename)

        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)
            
        return {"message": "File saved successfully"}
    except Exception as e:
        return {"message": e.args}
    