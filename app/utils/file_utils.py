from pathlib import Path
from fastapi import UploadFile
import shutil

def save_uploaded_file(file: UploadFile, destination: Path):
    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


def delete_file_if_exists(file_path: Path):
    if file_path.exists():
        file_path.unlink()

def delete_all_files_in_directory(directory: Path):
    for file_path in directory.iterdir():
        if file_path.is_file():
            file_path.unlink()