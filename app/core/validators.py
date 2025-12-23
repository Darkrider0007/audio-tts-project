import re
from fastapi import HTTPException, UploadFile
from .config import MAX_HINDI_WORDS, ALLOWED_AUDIO_FORMAT

def validate_hindi_text(text: str):
    words = text.strip().split()
    if len(words) > MAX_HINDI_WORDS:
        raise HTTPException(
            status_code=400,
            detail=f"Hindi text exceeds {MAX_HINDI_WORDS} words limit"
        )

def validate_wav_file(file: UploadFile):
    if not file.filename.lower().endswith(ALLOWED_AUDIO_FORMAT):
        raise HTTPException(
            status_code=400,
            detail="Only WAV audio files are allowed"
        )
