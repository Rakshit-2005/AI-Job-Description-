Write-Host "🔑 Getting Gemini API Key" -ForegroundColor Cyan
Write-Host "================================`n" -ForegroundColor Cyan

Write-Host "Follow these steps to get your free Gemini API key:`n" -ForegroundColor Yellow

Write-Host "1. Opening Google AI Studio in your browser..." -ForegroundColor Green
Start-Process "https://aistudio.google.com/app/apikey"

Write-Host "`n2. Sign in with your Google account" -ForegroundColor Green
Write-Host "3. Click 'Create API Key' button" -ForegroundColor Green
Write-Host "4. Copy the generated API key`n" -ForegroundColor Green

Write-Host "Waiting for you to get the API key..." -ForegroundColor Yellow
Write-Host "Press Enter once you have copied your API key..." -ForegroundColor Yellow
Read-Host

$apiKey = Read-Host "`nPaste your Gemini API key here"

if ($apiKey) {
    Write-Host "`nSaving API key to backend\.env..." -ForegroundColor Yellow
    
    $envPath = "backend\.env"
    
    if (Test-Path $envPath) {
        # Update existing .env file
        $content = Get-Content $envPath
        $newContent = $content -replace "GEMINI_API_KEY=.*", "GEMINI_API_KEY=$apiKey"
        $newContent | Set-Content $envPath
    } else {
        # Create from .env.example
        if (Test-Path "backend\.env.example") {
            $content = Get-Content "backend\.env.example"
            $newContent = $content -replace "GEMINI_API_KEY=.*", "GEMINI_API_KEY=$apiKey"
            $newContent | Set-Content $envPath
        } else {
            Write-Host "Error: .env.example not found!" -ForegroundColor Red
            exit
        }
    }
    
    Write-Host "`n✅ API Key saved successfully!" -ForegroundColor Green
    Write-Host "`nYou can now run the application:" -ForegroundColor Cyan
    Write-Host "  .\run.ps1" -ForegroundColor White
    Write-Host "`nOr manually:" -ForegroundColor Cyan
    Write-Host "  Backend: cd backend; .\venv\Scripts\Activate.ps1; uvicorn main:app --reload" -ForegroundColor White
    Write-Host "  Frontend: cd frontend; npm run dev" -ForegroundColor White
} else {
    Write-Host "`n❌ No API key provided" -ForegroundColor Red
    Write-Host "Please run this script again when you have your API key" -ForegroundColor Yellow
}

Write-Host "`n📚 Free Tier Limits:" -ForegroundColor Cyan
Write-Host "  • 60 requests per minute" -ForegroundColor White
Write-Host "  • 1,500 requests per day" -ForegroundColor White
Write-Host "  • Sufficient for hackathon development!`n" -ForegroundColor Green
