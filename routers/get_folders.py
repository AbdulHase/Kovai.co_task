import os
from fastapi import APIRouter

router = APIRouter()
BASE_DIR = "MyDrive"

@router.get("/folders")
def get_all_folders():
    """List all folders in base directory."""
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    folders = [name for name in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, name))]
    return {"folders": folders}