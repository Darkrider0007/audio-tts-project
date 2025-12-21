# Audio TTS Project

A comprehensive text-to-speech solution featuring Hindi TTS and voice cloning capabilities using Chatterbox.

## 📋 Project Structure

```
audio-tts-project/
├── hindi-tts/              # Hindi Text-to-Speech module
│   ├── src/
│   │   ├── config.py
│   │   ├── hindi_tts.py
│   │   └── hindi_voice_clone.py
│   ├── audio/
│   │   ├── input/
│   │   └── output/
│   ├── run_hindi.py
│   └── requirements.txt
├── chatterbox-cpu/         # Virtual environment with dependencies
├── README.md
├── .gitignore
└── CONTRIBUTING.md
```

## 🚀 Features

- **Hindi Text-to-Speech**: Convert Hindi text to speech
- **Voice Cloning**: Clone voices using advanced ML models
- **CPU-Optimized**: Works efficiently on CPU-based systems
- **Modular Architecture**: Easy to extend and customize

## 📦 Installation

### Prerequisites
- Python 3.10 - 3.11 
- Git
- Windows (for batch/PowerShell scripts) or Linux/Mac (use manual setup)

### Quick Setup (Windows)

**Option 1: Automated Setup (Recommended)**

1. **Clone the repository**
   ```bash
   git clone https://github.com/Darkrider0007/audio-tts-project
   cd audio-tts-project
   ```

2. **Run the setup script** (Choose one):
   - **PowerShell** (Recommended):
     ```powershell
     .\setup.ps1
     ```

The script will automatically:
- Create a virtual environment
- Activate the venv
- Upgrade pip
- Install all dependencies
- Verify the installation

**Option 2: Manual Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/audio-tts-project.git
   cd audio-tts-project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Activate on Linux/Mac:
   source venv/bin/activate
   ```

3. **Upgrade pip**
   ```bash
   python -m pip install --upgrade pip
   ```

4. **Install dependencies**
   ```bash
   cd hindi-tts
   pip install -r requirements.txt
   ```

5. **Verify installation** (optional)
   ```bash
   python -c "import torch; import torchaudio; print('Setup successful!')"
   ```

## 🎯 Usage

### Quick Start
Upload your audio file to the following directory:

```
hindi-tts/audio/input/
```
Ensure your audio file is in `.wav` format, noise-free, and between 5–15 seconds long. Update the filename reference in `run_hindi.py` accordingly.

```bash
# Navigate to the hindi-tts directory
cd hindi-tts

# Run the example script
python run_hindi.py
```


### Directory Structure After Setup

```
audio-tts-project/
├── venv/                       # Virtual environment (created by setup)
├── hindi-tts/
│   ├── src/
│   │   ├── config.py          # Configuration settings
│   │   ├── hindi_tts.py       # Main TTS engine
│   │   ├── hindi_voice_clone.py # Voice cloning module
│   │   └── __init__.py
│   ├── audio/
│   │   ├── input/             # Input audio files
│   │   └── output/            # Generated audio files
│   ├── run_hindi.py           # Example script
│   └── requirements.txt        # Python dependencies
├── setup.ps1                  # PowerShell setup script
├── setup.bat                  # Batch setup script
├── README.md                  # This file
├── CONTRIBUTING.md            # Contribution guidelines
├── .gitignore                 # Git ignore rules
└── LICENSE                    # License file
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work*
- [Contributors](https://github.com/yourusername/audio-tts-project/graphs/contributors)

## 🙏 Acknowledgments

- [Chatterbox TTS](https://github.com/pndurette/chatterbox) - TTS library
- [Diffusers](https://github.com/huggingface/diffusers) - For voice cloning
- [PyTorch](https://pytorch.org/) - Deep learning framework
- [Librosa](https://librosa.org/) - Audio processing
- All contributors and community members

## 🤔 Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError: No module named 'torch'"**
- Solution: Run `pip install -r hindi-tts/requirements.txt` again
- Or use the automated setup script: `.\setup.ps1`

**Issue: "Python is not recognized"**
- Solution: Add Python to your PATH or use full path to python.exe
- Restart terminal after installing Python

**Issue: Virtual environment won't activate**
- Solution: Run PowerShell as Administrator
- Or use: `venv\Scripts\Activate.ps1`

**Issue: Audio output files not created**
- Solution: Ensure `audio/output/` directory exists and has write permissions
- Check available disk space
