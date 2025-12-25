from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from pathlib import Path
from app.main import app

client = TestClient(app)

@patch("app.api.routes.FileResponse")
@patch("app.api.routes.generate_tts")
@patch("app.api.routes.validate_hindi_text")
@patch("app.api.routes.delete_all_files_in_directory")
def test_tts_api_success(mock_delete, mock_validate, mock_generate_tts, mock_file_response):
    """Test TTS API endpoint with mocked service"""
    output_path = Path("output/tts_output.wav")
    mock_generate_tts.return_value = output_path
    mock_file_response.return_value = MagicMock(status_code=200)

    response = client.post(
        "/tts",
        data={"text": "नमस्ते दुनिया"}
    )

    assert response.status_code == 200
    mock_validate.assert_called_once()
    mock_generate_tts.assert_called_once()
    mock_delete.assert_called_once()
