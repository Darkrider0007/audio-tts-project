from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from io import BytesIO
from app.main import app

client = TestClient(app)

@patch("app.api.routes.FileResponse")
@patch("app.api.routes.generate_voice_clone")
@patch("app.api.routes.validate_wav_file")
@patch("app.api.routes.validate_hindi_text")
@patch("app.api.routes.save_uploaded_file")
@patch("app.api.routes.delete_file_if_exists")
@patch("app.api.routes.delete_all_files_in_directory")
def test_voice_clone_api_success(mock_delete_all, mock_delete_file, mock_save_file, 
                                  mock_validate_text, mock_validate_wav, mock_generate_clone, 
                                  mock_file_response):
    """Test voice clone API endpoint with mocked service"""
    mock_generate_clone.return_value = None
    mock_file_response.return_value = MagicMock(status_code=200)

    response = client.post(
        "/voice-clone",
        data={"text": "नमस्ते दुनिया"},
        files={"audio": ("sample.wav", BytesIO(b"RIFF" + b"\x00" * 100), "audio/wav")}
    )

    assert response.status_code == 200
    mock_validate_text.assert_called_once()
    mock_validate_wav.assert_called_once()
    mock_save_file.assert_called_once()
    mock_generate_clone.assert_called_once()
    mock_delete_file.assert_called_once()
