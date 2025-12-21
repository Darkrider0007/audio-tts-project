import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from .config import DEVICE, AUDIO_OUTPUT_DIR

def generate_hindi_speech(text: str, filename: str = "hindi.wav"):
    model = ChatterboxMultilingualTTS.from_pretrained(device=DEVICE)

    wav = model.generate(
        text=text,
        language_id="hi"
    )

    output_path = AUDIO_OUTPUT_DIR / filename
    ta.save(str(output_path), wav, model.sr)

    print(f"Saved audio: {output_path}")
