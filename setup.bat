@echo off
REM Audio TTS Project Setup Script for Windows
REM This batch file runs the PowerShell setup script

setlocal enabledelayedexpansion

echo.
echo ========================================
echo Audio TTS Project Setup
echo ========================================
echo.

REM Check if PowerShell is available
powershell -Command "exit 0" >nul 2>&1
if errorlevel 1 (
    echo Error: PowerShell is required but not found
    exit /b 1
)

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

REM Run the PowerShell setup script with proper execution policy
powershell -ExecutionPolicy Bypass -File "%SCRIPT_DIR%setup.ps1" %*

if errorlevel 1 (
    echo.
    echo Setup encountered an error. Please check the messages above.
    pause
    exit /b 1
)

echo.
pause
