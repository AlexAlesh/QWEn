@echo off
REM DiLS — Development server (Windows)
setlocal

cd /d "%~dp0\.."

REM Activate virtual environment if exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

REM Load .env if exists
if exist ".env" (
    for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
        set "%%A=%%B"
    )
)

echo Starting DiLS in development mode...
echo   Host: %HOST%:%PORT%
echo   Debug: %DEBUG%
echo.

uvicorn app.main:app ^
    --host %HOST% ^
    --port %PORT% ^
    --reload ^
    --log-level info
