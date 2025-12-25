from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_tts_endpoint_exists():
    """Test that the /tts endpoint exists"""
    response = client.post(
        "/tts",
        data={"text": "नमस्ते दुनिया"}
    )
    # Should not return 404 - endpoint should exist
    assert response.status_code != 404


@patch("app.api.routes.FileResponse")
@patch("app.api.routes.generate_voice_clone")
@patch("app.api.routes.validate_wav_file")
@patch("app.api.routes.validate_hindi_text")
@patch("app.api.routes.save_uploaded_file")
@patch("app.api.routes.delete_file_if_exists")
@patch("app.api.routes.delete_all_files_in_directory")
def test_voice_clone_endpoint_exists(mock_delete_all, mock_delete_file, mock_save_file, 
                                      mock_validate_text, mock_validate_wav, mock_generate_clone, 
                                      mock_file_response):
    """Test that the /voice-clone endpoint exists"""
    mock_generate_clone.return_value = None
    mock_file_response.return_value = MagicMock(status_code=200)
    
    response = client.post(
        "/voice-clone",
        data={"text": "नमस्ते दुनिया"},
        files={"audio": ("sample.wav", b"RIFF" + b"\x00" * 100, "audio/wav")}
    )
    # Should not return 404 - endpoint should exist
    assert response.status_code != 404