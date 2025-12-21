import torch

# --- FORCE ALL TORCH LOADS TO CPU (CRITICAL FIX) ---
_original_torch_load = torch.load

def cpu_torch_load(*args, **kwargs):
    kwargs["map_location"] = torch.device("cpu")
    return _original_torch_load(*args, **kwargs)

torch.load = cpu_torch_load
# --------------------------------------------------

from src.hindi_tts import generate_hindi_speech
from src.hindi_voice_clone import generate_hindi_voice_clone

if __name__ == "__main__":
    text = (
        "नमस्ते! यह एक हिंदी पाठ से भाषण उत्पन्न करने और आवाज़ क्लोनिंग उदाहरण है।"
    )

    # generate_hindi_speech(text, filename="hindi.wav")

    generate_hindi_voice_clone(
        text=text,
        prompt_filename="voice.wav",
        output_filename="voice.wav"
    )
