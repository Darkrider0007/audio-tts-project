from pathlib import Path

DEVICE = "cpu"

BASE_DIR = Path(__file__).resolve().parent.parent
AUDIO_INPUT_DIR = BASE_DIR / "audio" / "input"
AUDIO_OUTPUT_DIR = BASE_DIR / "audio" / "output"

AUDIO_INPUT_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
