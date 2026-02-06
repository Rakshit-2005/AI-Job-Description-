Write-Host "🧪 Testing AI Assessment Platform" -ForegroundColor Cyan
Write-Host "==================================`n" -ForegroundColor Cyan

$baseUrl = "http://localhost:8000"

function Test-Backend {
    Write-Host "Testing backend connection..." -ForegroundColor Yellow
    try {
        $response = Invoke-WebRequest -Uri "$baseUrl/" -Method GET -TimeoutSec 5
        if ($response.StatusCode -eq 200) {
            Write-Host "✅ Backend is running!" -ForegroundColor Green
            return $true
        }
    } catch {
        Write-Host "❌ Backend is not running!" -ForegroundColor Red
        Write-Host "Please start backend: cd backend; .\venv\Scripts\Activate.ps1; uvicorn main:app --reload" -ForegroundColor Yellow
        return $false
    }
}

function Test-Frontend {
    Write-Host "Testing frontend connection..." -ForegroundColor Yellow
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:5173" -Method GET -TimeoutSec 5
        if ($response.StatusCode -eq 200) {
            Write-Host "✅ Frontend is running!" -ForegroundColor Green
            return $true
        }
    } catch {
        Write-Host "❌ Frontend is not running!" -ForegroundColor Red
        Write-Host "Please start frontend: cd frontend; npm run dev" -ForegroundColor Yellow
        return $false
    }
}

function Test-GeminiKey {
    Write-Host "Checking Gemini API key..." -ForegroundColor Yellow
    
    if (Test-Path "backend\.env") {
        $envContent = Get-Content "backend\.env"
        $keyLine = $envContent | Where-Object { $_ -match "GEMINI_API_KEY=" }
        
        if ($keyLine -and $keyLine -match "GEMINI_API_KEY=.+") {
            $key = $keyLine -replace "GEMINI_API_KEY=", ""
            if ($key -ne "your_gemini_api_key_here" -and $key.Length -gt 10) {
                Write-Host "✅ Gemini API key is configured!" -ForegroundColor Green
                return $true
            }
        }
        
        Write-Host "❌ Gemini API key not configured!" -ForegroundColor Red
        Write-Host "Run: .\get-api-key.ps1 to configure" -ForegroundColor Yellow
        return $false
    } else {
        Write-Host "❌ .env file not found!" -ForegroundColor Red
        Write-Host "Run: .\setup.ps1 first" -ForegroundColor Yellow
        return $false
    }
}

function Test-Dependencies {
    Write-Host "Checking dependencies..." -ForegroundColor Yellow
    
    # Check Python
    try {
        $pythonVersion = python --version 2>&1
        Write-Host "✅ Python installed: $pythonVersion" -ForegroundColor Green
    } catch {
        Write-Host "❌ Python not found!" -ForegroundColor Red
        return $false
    }
    
    # Check Node.js
    try {
        $nodeVersion = node --version 2>&1
        Write-Host "✅ Node.js installed: $nodeVersion" -ForegroundColor Green
    } catch {
        Write-Host "❌ Node.js not found!" -ForegroundColor Red
        return $false
    }
    
    # Check if venv exists
    if (Test-Path "backend\venv") {
        Write-Host "✅ Python virtual environment exists" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Virtual environment not found" -ForegroundColor Yellow
        Write-Host "Run: .\setup.ps1" -ForegroundColor Yellow
    }
    
    # Check if node_modules exists
    if (Test-Path "frontend\node_modules") {
        Write-Host "✅ Node modules installed" -ForegroundColor Green
    } else {
        Write-Host "⚠️  Node modules not found" -ForegroundColor Yellow
        Write-Host "Run: cd frontend; npm install" -ForegroundColor Yellow
    }
    
    return $true
}

function Show-Status {
    Write-Host "`n📊 System Status" -ForegroundColor Cyan
    Write-Host "================" -ForegroundColor Cyan
    
    $backendRunning = Test-Backend
    $frontendRunning = Test-Frontend
    $geminiConfigured = Test-GeminiKey
    $depsInstalled = Test-Dependencies
    
    Write-Host "`n📝 Summary:" -ForegroundColor Cyan
    
    if ($backendRunning -and $frontendRunning -and $geminiConfigured) {
        Write-Host "✅ All systems operational!" -ForegroundColor Green
        Write-Host "`nYou can access:" -ForegroundColor Cyan
        Write-Host "  Frontend: http://localhost:5173" -ForegroundColor White
        Write-Host "  Backend: http://localhost:8000" -ForegroundColor White
        Write-Host "  API Docs: http://localhost:8000/docs" -ForegroundColor White
    } else {
        Write-Host "⚠️  Some issues detected. Please fix them and try again." -ForegroundColor Yellow
    }
}

function Create-TestData {
    Write-Host "`n🎯 Creating test data..." -ForegroundColor Cyan
    
    Write-Host "Opening SAMPLE_DATA.md with test job descriptions..." -ForegroundColor Yellow
    
    if (Test-Path "SAMPLE_DATA.md") {
        Start-Process notepad "SAMPLE_DATA.md"
        Write-Host "✅ Sample data file opened!" -ForegroundColor Green
        Write-Host "Use these job descriptions to test the platform" -ForegroundColor White
    } else {
        Write-Host "❌ SAMPLE_DATA.md not found!" -ForegroundColor Red
    }
}

# Main execution
Write-Host "Starting system checks...`n" -ForegroundColor Yellow

Show-Status

Write-Host "`n"
$choice = Read-Host "Do you want to view sample test data? (y/n)"
if ($choice -eq "y" -or $choice -eq "Y") {
    Create-TestData
}

Write-Host "`n✨ Testing complete!`n" -ForegroundColor Green
