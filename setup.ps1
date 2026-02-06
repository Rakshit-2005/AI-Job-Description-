# Setup Backend
Write-Host "Setting up Backend..." -ForegroundColor Green
Set-Location backend

# Create virtual environment
Write-Host "Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

# Install dependencies
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

# Create .env file if not exists
if (-not (Test-Path .env)) {
    Write-Host "Creating .env file..." -ForegroundColor Yellow
    Copy-Item .env.example .env
    Write-Host "⚠️  Please edit backend\.env and add your GEMINI_API_KEY" -ForegroundColor Red
}

Set-Location ..

# Setup Frontend
Write-Host "`nSetting up Frontend..." -ForegroundColor Green
Set-Location frontend

# Install npm dependencies
Write-Host "Installing npm dependencies..." -ForegroundColor Yellow
npm install

Set-Location ..

Write-Host "`n✅ Setup Complete!" -ForegroundColor Green
Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "1. Edit backend\.env and add your Gemini API key"
Write-Host "2. Start backend: cd backend; .\venv\Scripts\Activate.ps1; uvicorn main:app --reload"
Write-Host "3. Start frontend (new terminal): cd frontend; npm run dev"
Write-Host "`nBackend will run on: http://localhost:8000"
Write-Host "Frontend will run on: http://localhost:5173"
