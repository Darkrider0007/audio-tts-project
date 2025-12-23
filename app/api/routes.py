from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from pathlib import Path

from app.core.validators import validate_hindi_text, validate_wav_file
from app.core.config import INPUT_DIR, OUTPUT_DIR
from app.utils.file_utils import delete_all_files_in_directory, delete_file_if_exists, save_uploaded_file
from app.services.tts_service import generate_tts
from app.services.voice_clone_service import generate_voice_clone

router = APIRouter()

@router.post("/tts")
def text_to_audio(
    text: str = Form(...),
    outputName: str = Form("tts_output.wav")
):
    delete_all_files_in_directory(OUTPUT_DIR)
    validate_hindi_text(text)

    # FULL FILE PATH (not directory)
    output_file = OUTPUT_DIR / outputName

    # IMPORTANT: capture returned file path
    generated_file = generate_tts(text, output_file)

    return FileResponse(
        path=generated_file,
        media_type="audio/wav",
        filename=outputName
    )


@router.post("/voice-clone")
def voice_clone(
    text: str = Form(...),
    audio: UploadFile = File(...),
    outputName: str = Form("voice_clone_output.wav")
):
    delete_all_files_in_directory(OUTPUT_DIR)
    validate_hindi_text(text)
    validate_wav_file(audio)

    input_audio_path = INPUT_DIR / audio.filename
    save_uploaded_file(audio, input_audio_path)

    output_file = OUTPUT_DIR / outputName
    generate_voice_clone(input_audio_path, text, output_file)

    delete_file_if_exists(input_audio_path)

    return FileResponse(
        output_file,
        media_type="audio/wav",
        filename=outputName
    )
