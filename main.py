from fastapi import FastAPI
from routers import get_folders, create_folder, update_folder, delete_folder

app = FastAPI(title="Migration Task Folder API")

app.include_router(get_folders.router)
app.include_router(create_folder.router)
app.include_router(update_folder.router)
app.include_router(delete_folder.router)
