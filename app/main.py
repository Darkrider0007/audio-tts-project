from fastapi import FastAPI
from app.api.routes import router
import torch

# --- FORCE ALL TORCH LOADS TO CPU (CRITICAL FIX) ---
_original_torch_load = torch.load

def cpu_torch_load(*args, **kwargs):
    kwargs["map_location"] = torch.device("cpu")
    return _original_torch_load(*args, **kwargs)

torch.load = cpu_torch_load
# --------------------------------------------------

app = FastAPI(
    title="Hindi TTS & Voice Cloning API",
    description="Text-to-Speech and Voice Cloning (WAV only)",
    version="1.0.0"
)

app.include_router(router)
