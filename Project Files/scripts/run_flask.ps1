# Run Flask DR Screening App
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Starting Flask DR Screening Server..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🌐 Landing Page: http://localhost:5000/" -ForegroundColor Yellow
Write-Host "🔬 Main App: http://localhost:5000/app" -ForegroundColor Yellow
Write-Host "📡 API: http://localhost:5000/api/predict" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""
cd c:\Users\chips\Desktop\dldr
python flask_app.py
