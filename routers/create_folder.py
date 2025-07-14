import os
from fastapi import APIRouter, Body

router = APIRouter()
BASE_DIR = "MyDrive"

@router.post("/folders")
def create_folder(folder_name: str = Body(..., embed=True)):
    """Create a new folder."""
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    folder_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        return {"message": f"Folder '{folder_name}' created successfully."}
    else:
        return {"message": f"Folder '{folder_name}' already exists."}