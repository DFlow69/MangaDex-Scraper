# Install requirements for MangaDex Scraper
$ErrorActionPreference = "Stop"

function Install-Python {
    Write-Host "Python not found. Attempting to install Python via winget..." -ForegroundColor Yellow
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host "Installing Python 3.12..." -ForegroundColor Cyan
        winget install --id Python.Python.3.12 --exact --silent --accept-package-agreements --accept-source-agreements
        
        # Refresh environment variables to recognize the new python command
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
        
        if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
            Write-Host "Python was installed but is not yet in the PATH. You may need to restart your terminal." -ForegroundColor Red
            return $false
        }
        return $true
    } else {
        Write-Host "winget not found. Please install Python manually from https://python.org" -ForegroundColor Red
        return $false
    }
}

Write-Host "Checking for Python..." -ForegroundColor Cyan

$pythonCmd = ""
if (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonCmd = "python"
} elseif (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonCmd = "py"
} else {
    if (Install-Python) {
        $pythonCmd = "python"
    } else {
        Pause
        exit
    }
}

Write-Host "Using $pythonCmd to install libraries..." -ForegroundColor Cyan

# Ensure pip is available and updated
& $pythonCmd -m pip install --upgrade pip --quiet

# Install all requirements
$libs = @("requests", "questionary", "rich", "prompt_toolkit", "tqdm", "Pillow", "PySide6")
Write-Host "Installing dependencies: $($libs -join ', ')..." -ForegroundColor Cyan
& $pythonCmd -m pip install $libs --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "Installation complete! You can now run the scraper." -ForegroundColor Green
} else {
    Write-Host "Installation finished with errors. You might need to run this as Administrator." -ForegroundColor Red
}

Pause
