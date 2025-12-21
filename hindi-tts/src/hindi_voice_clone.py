import torchaudio as ta
from chatterbox.mtl_tts import ChatterboxMultilingualTTS
from .config import DEVICE, AUDIO_INPUT_DIR, AUDIO_OUTPUT_DIR

def generate_hindi_voice_clone(
    text: str,
    prompt_filename: str = "voice.wav",
    output_filename: str = "hindi_clone.wav"
):
    model = ChatterboxMultilingualTTS.from_pretrained(device=DEVICE)

    prompt_path = AUDIO_INPUT_DIR / prompt_filename

    if not prompt_path.exists():
        raise FileNotFoundError(f"Voice prompt not found: {prompt_path}")

    wav = model.generate(
        text=text,
        language_id="hi",
        audio_prompt_path=str(prompt_path)
    )

    output_path = AUDIO_OUTPUT_DIR / output_filename
    ta.save(str(output_path), wav, model.sr)

    print(f"Voice-cloned audio saved at: {output_path}")
