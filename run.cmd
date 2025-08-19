@echo off
chcp 65001 >nul
cd /d "%~dp0"

if not exist "venv" call setup.cmd
if not exist "venv" (
    echo ❌ Не удалось создать окружение
    pause
    exit /b 1
)

call venv\Scripts\activate.bat
python src/main.py
pause