import os
import shutil
from fastapi import APIRouter, Path

router = APIRouter()
BASE_DIR = "MyDrive"

@router.delete("/folders/{folder_name}")
def delete_folder(folder_name: str = Path(...)):
    """Delete a folder."""
    folder_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.exists(folder_path):
        return {"message": f"Folder '{folder_name}' does not exist."}
    shutil.rmtree(folder_path)
    return {"message": f"Folder '{folder_name}' deleted successfully."}