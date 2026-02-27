# Run Landing Page Server
Write-Host "Starting Landing Page Server..." -ForegroundColor Green
Write-Host "Landing page will be available at: http://localhost:8000" -ForegroundColor Cyan
Write-Host ""
cd c:\Users\chips\Desktop\dldr
python -m http.server 8000
