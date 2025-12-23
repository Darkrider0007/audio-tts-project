from pathlib import Path
import torchaudio
import torch
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from app.core.config import DEVICE


_MODEL = None


def _load_model():
    """
    Lazy-load voice cloning model.
    """
    global _MODEL
    if _MODEL is None:
        # Replace with your actual CLI model loader
       _MODEL = ChatterboxMultilingualTTS.from_pretrained(device=DEVICE)
    return _MODEL


def generate_voice_clone(
    reference_audio: Path,
    text: str,
    output_path: Path
) -> Path:
    """
    Generate cloned voice speech using a reference WAV file.

    Args:
        reference_audio (Path): Input WAV file (saved in inputs/)
        text (str): Hindi text
        output_path (Path): Output WAV file

    Returns:
        Path: Generated WAV file
    """
    model = _load_model()

    with torch.no_grad():
        cloned_wav = model.generate(
            text=text,
            language_id="hi",
            audio_prompt_path=str(reference_audio)
        )

    if cloned_wav.dim() == 1:
        cloned_wav = cloned_wav.unsqueeze(0)

    torchaudio.save(str(output_path), cloned_wav, model.sr)
    return output_path
