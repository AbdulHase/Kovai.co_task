import os
from fastapi import APIRouter, Body, Path

router = APIRouter()
BASE_DIR = "MyDrive"

@router.put("/folders/{old_name}")
def update_folder(old_name: str = Path(...), new_name: str = Body(..., embed=True)):
    """Rename an existing folder."""
    old_path = os.path.join(BASE_DIR, old_name)
    new_path = os.path.join(BASE_DIR, new_name)
    if not os.path.exists(old_path):
        return {"message": f"Folder '{old_name}' does not exist."}
    if os.path.exists(new_path):
        return {"message": f"Folder '{new_name}' already exists."}
    os.rename(old_path, new_path)
    return {"message": f"Folder renamed from '{old_name}' to '{new_name}' successfully."}