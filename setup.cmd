@echo off
chcp 65001 >nul
cd /d "%~dp0"

:: Проверка Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python не найден в PATH.
    pause
    exit /b 1
)

:: Создаём config.ini, если нет
if not exist "config.ini" (
    >config.ini (
        echo [Paths]
        echo game_path = C:/Games/MyAwesomeGame
        echo.
        echo [Settings]
        echo fullscreen = True
        echo resolution = 1920x1080
    )
    echo + config.ini создан
)

:: Создаём venv, если нет
if not exist "venv" (
    python -m venv venv
    if %errorlevel% neq 0 (
        echo ❌ Ошибка создания venv
        pause
        exit /b 1
    )
    echo + venv создан
)

:: Активируем и устанавливаем зависимости, если есть requirements.txt
call venv\Scripts\activate.bat

:: Обновляем pip тихо
python -m pip install --upgrade pip >nul 2>&1

:: Устанавливаем зависимости, если файл есть
if exist "requirements.txt" (
    pip install -q -r requirements.txt
    echo + Пакеты установлены из requirements.txt
)

echo ✅ Готово. Запускайте run.cmd
deactivate
pause