# Audio TTS Project Setup Script for Windows
# This script automates the setup process after cloning the repository

param(
    [switch]$SkipVenv = $false,
    [switch]$Help = $false
)

function Show-Help {
    Write-Host @"
Audio TTS Project Setup Script
==============================

Usage:
    .\setup.ps1 [OPTIONS]

Options:
    -SkipVenv    Skip virtual environment creation (use existing venv)
    -Help        Show this help message

Examples:
    .\setup.ps1                    # Full setup
    .\setup.ps1 -SkipVenv          # Skip venv, just install requirements
    .\setup.ps1 -Help              # Show help

"@
}

function Write-Header {
    param([string]$Message)
    Write-Host ""
    Write-Host "=" * 60 -ForegroundColor Cyan
    Write-Host $Message -ForegroundColor Cyan
    Write-Host "=" * 60 -ForegroundColor Cyan
    Write-Host ""
}

function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Error-Message {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host "ℹ $Message" -ForegroundColor Yellow
}

# Show help if requested
if ($Help) {
    Show-Help
    exit 0
}

# Start setup
Write-Header "Audio TTS Project Setup"

# Check if Python is installed
Write-Info "Checking Python installation..."
try {
    $pythonVersion = python --version 2>&1
    Write-Success "Python found: $pythonVersion"
} catch {
    Write-Error-Message "Python is not installed or not in PATH"
    Write-Host "Please install Python 3.8+ from https://www.python.org/"
    exit 1
}

# Check if Git is installed
Write-Info "Checking Git installation..."
try {
    $gitVersion = git --version
    Write-Success "Git found: $gitVersion"
} catch {
    Write-Error-Message "Git is not installed or not in PATH"
    exit 1
}

# Get the script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Info "Project directory: $scriptDir"

# Check if we're in the correct directory
if (-not (Test-Path (Join-Path $scriptDir "hindi-tts"))) {
    Write-Error-Message "hindi-tts directory not found!"
    Write-Host "Please run this script from the project root directory"
    exit 1
}

Write-Success "Project structure verified"

# Create virtual environment if not skipping
if (-not $SkipVenv) {
    Write-Header "Creating Virtual Environment"
    
    if (Test-Path (Join-Path $scriptDir "venv")) {
        Write-Info "Virtual environment already exists"
        $createNew = Read-Host "Do you want to recreate it? (y/n)"
        if ($createNew -eq 'y') {
            Write-Info "Removing existing virtual environment..."
            Remove-Item -Path (Join-Path $scriptDir "venv") -Recurse -Force
            Write-Success "Old venv removed"
        }
    }
    
    if (-not (Test-Path (Join-Path $scriptDir "venv"))) {
        Write-Info "Creating new virtual environment..."
        python -m venv venv
        
        if ($LASTEXITCODE -eq 0) {
            Write-Success "Virtual environment created"
        } else {
            Write-Error-Message "Failed to create virtual environment"
            exit 1
        }
    }
} else {
    Write-Info "Skipping virtual environment creation"
}

# Activate virtual environment
Write-Header "Activating Virtual Environment"
$venvPath = Join-Path $scriptDir "venv\Scripts\Activate.ps1"

if (Test-Path $venvPath) {
    & $venvPath
    Write-Success "Virtual environment activated"
} else {
    Write-Error-Message "Virtual environment activation script not found"
    exit 1
}

# Upgrade pip
Write-Header "Upgrading pip"
Write-Info "This may take a moment..."
python -m pip install --upgrade pip
if ($LASTEXITCODE -eq 0) {
    Write-Success "pip upgraded successfully"
} else {
    Write-Error-Message "Failed to upgrade pip"
}

# Install requirements
Write-Header "Installing Project Dependencies"
$reqFile = Join-Path $scriptDir "hindi-tts\requirements.txt"

if (Test-Path $reqFile) {
    Write-Info "Installing from requirements.txt..."
    Write-Info "This may take several minutes..."
    pip install -r $reqFile
    
    if ($LASTEXITCODE -eq 0) {
        Write-Success "All dependencies installed successfully"
    } else {
        Write-Error-Message "Failed to install some dependencies"
        Write-Host "Try running: pip install -r hindi-tts/requirements.txt" -ForegroundColor Yellow
    }
} else {
    Write-Error-Message "requirements.txt not found at $reqFile"
    exit 1
}

# Verify installation
Write-Header "Verifying Installation"
Write-Info "Checking key packages..."

$packages = @("torch", "torchaudio", "chatterbox", "librosa", "soundfile")
$allInstalled = $true

foreach ($package in $packages) {
    try {
        python -c "import $package" 2>&1 | Out-Null
        Write-Success "$package is installed"
    } catch {
        Write-Error-Message "$package is NOT installed"
        $allInstalled = $false
    }
}

# Final summary
Write-Header "Setup Complete!"

if ($allInstalled) {
    Write-Success "All systems ready!"
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Cyan
    Write-Host "1. Navigate to the hindi-tts directory: cd hindi-tts"
    Write-Host "2. Review the code in src/ directory"
    Write-Host "3. Run the example: python run_hindi.py"
    Write-Host ""
} else {
    Write-Info "Setup completed with some warnings"
    Write-Host "Please check the errors above and install missing packages manually"
}

Write-Host ""
Write-Info "Virtual environment will remain activated in this terminal"
Write-Info "To deactivate later, type: deactivate"
Write-Host ""
