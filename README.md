# Audio TTS API (Hindi TTS & Voice Cloning)

FastAPI service that provides Hindi Text-to-Speech and simple voice cloning. CPU-only by design — all PyTorch model loads are forced to CPU in [app/main.py](app/main.py).

## Project Structure

```text
audio-tts-project/
├─ app/
│  ├─ main.py                 # FastAPI app factory and CPU safety for torch
│  ├─ api/
│  │  └─ routes.py            # HTTP endpoints (/tts, /voice-clone)
│  ├─ core/
│  │  ├─ config.py            # Paths and simple config
│  │  └─ validators.py        # Input validation
│  ├─ services/
│  │  ├─ tts_service.py       # Hindi TTS service
│  │  └─ voice_clone_service.py # Voice cloning service
│  └─ utils/
│     └─ file_utils.py        # File utilities
├─ tests/
│  ├─ test_health.py          # Health check tests
│  ├─ test_tts_api.py         # TTS endpoint tests
│  └─ test_voice_clone_api.py # Voice clone endpoint tests
├─ inputs/                    # Temp storage for uploaded source audio
├─ outputs/                   # Generated WAV files
├─ requirements.txt           # Python dependencies
├─ setup.ps1                  # Windows one-step setup
├─ pytest.ini                 # Pytest configuration
└─ README.md
```

## Requirements

- Python 3.10 or 3.11
- Windows PowerShell (for setup.ps1) or any shell for manual setup

## Setup

### Option A — One-step (Windows)

```powershell
git clone https://github.com/Darkrider0007/audio-tts-project
cd audio-tts-project
./setup.ps1
```

What it does:

- Creates and activates a virtual environment
- Upgrades pip and installs from requirements.txt
- Ensures `inputs/` and `outputs/` exist

### Option B — Manual (any OS)

```bash
git clone https://github.com/Darkrider0007/audio-tts-project
cd audio-tts-project
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run The API

```bash
uvicorn app.main:app --reload
```

- Local server: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

The API object is defined in [app/main.py](app/main.py) and routes are in [app/api/routes.py](app/api/routes.py).

## Testing

Run the test suite with:

```bash
python -m pytest tests/ -v
```

This runs all tests in the `tests/` directory with verbose output.

## API Overview

Notes (enforced by [app/core/config.py](app/core/config.py) and validators):

- Input audio must be WAV (`.wav`).
- Max 50 Hindi words per request.
- `outputs/` is cleared before each generation; only the latest file remains.

### POST /tts

Generate TTS from Hindi text.

Form fields:

- `text` (required): Hindi text
- `outputName` (optional): filename to save, default `tts_output.wav`

Returns: `audio/wav` file and writes it to `outputs/`.

Curl example:

```bash
curl -X POST http://127.0.0.1:8000/tts \
  -F "text=नमस्ते, आप कैसे हैं?" \
  -F "outputName=tts_output.wav" \
  -o tts_output.wav
```

### POST /voice-clone

Clone voice from a source WAV and synthesize the provided text.

Form fields:

- `text` (required): Hindi text
- `audio` (required): WAV file upload
- `outputName` (optional): filename to save, default `voice_clone_output.wav`

Returns: `audio/wav` file and writes it to `outputs/`.

Curl example (assumes `inputs/sample.wav` exists):

```bash
curl -X POST http://127.0.0.1:8000/voice-clone \
  -F "text=यह एक परीक्षण है" \
  -F "audio=@inputs/sample.wav;type=audio/wav" \
  -F "outputName=voice_clone_output.wav" \
  -o voice_clone_output.wav
```

## Tips & Troubleshooting

- CPU only: torch loads are mapped to CPU in [app/main.py](app/main.py).
- If `uvicorn` is not found, ensure your venv is active before running.
- A request clears `outputs/` first; copy files out if you need to keep history.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs and issues welcome!
