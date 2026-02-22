@echo off
setlocal EnableDelayedExpansion

REM Try to find python executable
where python >nul 2>nul
if %errorlevel% equ 0 (
    set PYTHON_CMD=python
    goto :FOUND
)

where python3 >nul 2>nul
if %errorlevel% equ 0 (
    set PYTHON_CMD=python3
    goto :FOUND
)

where py >nul 2>nul
if %errorlevel% equ 0 (
    set PYTHON_CMD=py
    goto :FOUND
)

echo.
echo [ERROR] Python was not found!
echo.
echo Troubleshooting steps:
echo 1. Ensure Python is installed from python.org or Microsoft Store.
echo 2. If installed from Microsoft Store, search for "Manage App Execution Aliases" in Windows Settings
echo    and ensure "python.exe" and "python3.exe" are turned ON.
echo 3. If installed from python.org, ensure "Add Python to PATH" was checked during installation.
echo.
pause
exit /b 1

:FOUND
echo Found Python: !PYTHON_CMD!
!PYTHON_CMD! md.py