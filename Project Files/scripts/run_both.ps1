# Run Both Servers Simultaneously
Write-Host "========================================" -ForegroundColor Yellow
Write-Host "Starting Both Servers..." -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Landing Page: http://localhost:8000" -ForegroundColor Cyan
Write-Host "2. Streamlit App: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop both servers" -ForegroundColor Yellow
Write-Host ""

cd c:\Users\chips\Desktop\dldr

# Start landing page server in background
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd c:\Users\chips\Desktop\dldr; Write-Host 'Landing Page Server (Port 8000)' -ForegroundColor Green; python -m http.server 8000"

# Wait a moment for the first server to start
Start-Sleep -Seconds 2

# Start Streamlit app (this will block)
Write-Host "Starting Streamlit App..." -ForegroundColor Green
streamlit run app.py
