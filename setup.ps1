# ===============================
# Audio TTS Project Setup Script
# ===============================

# Ensure UTF-8 output
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# -------------------------------
# Helper Functions
# -------------------------------
function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-Success {
    param([string]$Message)
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-Error-Message {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Print-Separator {
    Write-Host ("=" * 60)
}

# -------------------------------
# Script Start
# -------------------------------
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Print-Separator
Write-Host "Audio TTS Project Setup"
Print-Separator

# -------------------------------
# Check Python
# -------------------------------
Write-Info "Checking Python installation..."
try {
    $pythonVersion = python --version 2>&1
    Write-Success "Python found: $pythonVersion"
}
catch {
    Write-Error-Message "Python not found. Install Python 3.10 or 3.11"
    exit 1
}

# -------------------------------
# Check Git
# -------------------------------
Write-Info "Checking Git installation..."
try {
    $gitVersion = git --version 2>&1
    Write-Success "Git found: $gitVersion"
}
catch {
    Write-Error-Message "Git not found. Install Git"
    exit 1
}

# -------------------------------
# Virtual Environment Setup
# -------------------------------
Print-Separator
Write-Host "Virtual Environment Setup"
Print-Separator

$venvPath = Join-Path $scriptDir "venv"

if (Test-Path $venvPath) {
    Write-Info "Virtual environment already exists"
    $choice = Read-Host "Do you want to recreate it? (y/n)"

    if ($choice -match "^[Yy]$") {
        if ($env:VIRTUAL_ENV) {
            Write-Info "Deactivating active virtual environment"
            deactivate
        }

        Write-Info "Removing existing virtual environment..."
        try {
            Remove-Item -Path $venvPath -Recurse -Force -ErrorAction Stop
            Write-Success "Old venv removed"
        }
        catch {
            Write-Error-Message "Failed to remove venv. Close terminals and retry."
            exit 1
        }
    }
    else {
        Write-Info "Keeping existing virtual environment"
    }
}

if (-not (Test-Path $venvPath)) {
    Write-Info "Creating virtual environment..."
    python -m venv venv
    Write-Success "Virtual environment created"
}

# -------------------------------
# Activate Virtual Environment
# -------------------------------
Print-Separator
Write-Host "Activating Virtual Environment"
Print-Separator

$activateScript = Join-Path $venvPath "Scripts\Activate.ps1"

if (-not (Test-Path $activateScript)) {
    Write-Error-Message "Activation script not found"
    exit 1
}

Write-Info "Activating venv..."
& $activateScript
Write-Success "Virtual environment activated"

# -------------------------------
# Upgrade pip
# -------------------------------
Write-Info "Upgrading pip..."
python -m pip install --upgrade pip
Write-Success "pip upgraded"

# -------------------------------
# Install Hindi-TTS Requirements
# -------------------------------
Print-Separator
Write-Host "Installing Hindi-TTS Dependencies"
Print-Separator

$hindiTtsDir = Join-Path $scriptDir "hindi-tts"
$hindiReqFile = Join-Path $hindiTtsDir "requirements.txt"

if (-not (Test-Path $hindiTtsDir)) {
    Write-Error-Message "hindi-tts directory not found"
    exit 1
}

Push-Location $hindiTtsDir
Write-Info "Entered hindi-tts directory"

if (Test-Path $hindiReqFile) {
    Write-Info "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
    Write-Success "Hindi-TTS dependencies installed"
}
else {
    Write-Error-Message "requirements.txt not found inside hindi-tts"
    Pop-Location
    exit 1
}

Pop-Location

# -------------------------------
# Done
# -------------------------------
Print-Separator
Write-Success "Setup completed successfully"
Print-Separator
