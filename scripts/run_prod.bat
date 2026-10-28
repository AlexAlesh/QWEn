@echo off
REM DiLS — Production server (Windows)
setlocal

cd /d "%~dp0\.."

REM Activate virtual environment
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

REM Load .env
if exist ".env" (
    for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
        set "%%A=%%B"
    )
)

REM Ensure logs and backups dirs exist
if not exist "logs" mkdir logs
if not exist "backups" mkdir backups

set WORKERS=%WORKERS%
if "%WORKERS%"=="" set WORKERS=4
if "%HOST%"=="" set HOST=0.0.0.0
if "%PORT%"=="" set PORT=8000

echo Starting DiLS in production mode...
echo   Host: %HOST%:%PORT%
echo   Workers: %WORKERS%
echo.

uvicorn app.main:app ^
    --host %HOST% ^
    --port %PORT% ^
    --workers %WORKERS% ^
    --log-level info
