from pathlib import Path
import torchaudio
import torch
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from app.core.config import DEVICE

_MODEL = None


def _load_model():
    global _MODEL
    if _MODEL is None:
        _MODEL = ChatterboxMultilingualTTS.from_pretrained(device=DEVICE)
    return _MODEL


def generate_tts(text: str, output_path: Path) -> Path:
    model = _load_model()

    # Ensure file path
    if output_path.is_dir():
        output_path = output_path / "tts_output.wav"

    if output_path.suffix.lower() != ".wav":
        output_path = output_path.with_suffix(".wav")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with torch.no_grad():
        wav = model.generate(
            text=text,
            language_id="hi"
        )

    if wav.dim() == 1:
        wav = wav.unsqueeze(0)

    # IMPORTANT: positional args only
    torchaudio.save(
        str(output_path),
        wav.cpu(),
        model.sr
    )

    return output_path
