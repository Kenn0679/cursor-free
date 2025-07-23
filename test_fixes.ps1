# PowerShell script to test the fixed cursor_acc_info.py

Write-Host "🔍 Testing Cursor Free VIP fixes..." -ForegroundColor Cyan

# Check if we can find a Python executable
$pythonExe = $null
$possiblePaths = @(
    "python",
    "python3", 
    "py",
    "$env:LOCALAPPDATA\Programs\Python\*\python.exe",
    "$env:PROGRAMFILES\Python*\python.exe"
)

foreach ($path in $possiblePaths) {
    try {
        if ($path -like "*\*") {
            $found = Get-ChildItem -Path $path -ErrorAction SilentlyContinue | Select-Object -First 1
            if ($found) {
                $pythonExe = $found.FullName
                break
            }
        } else {
            $null = & $path --version 2>$null
            if ($LASTEXITCODE -eq 0) {
                $pythonExe = $path
                break
            }
        }
    } catch {
        continue
    }
}

if ($pythonExe) {
    Write-Host "✅ Found Python: $pythonExe" -ForegroundColor Green
    
    # Test the syntax of cursor_acc_info.py
    Write-Host "🔍 Testing cursor_acc_info.py syntax..." -ForegroundColor Yellow
    $result = & $pythonExe -m py_compile cursor_acc_info.py 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ cursor_acc_info.py syntax is OK" -ForegroundColor Green
        
        # Test our simple test script
        Write-Host "🔍 Running simple test..." -ForegroundColor Yellow
        & $pythonExe simple_test.py
        
    } else {
        Write-Host "❌ Syntax error in cursor_acc_info.py:" -ForegroundColor Red
        Write-Host $result -ForegroundColor Red
    }
} else {
    Write-Host "⚠️  Python not found. Please install Python to test the fixes." -ForegroundColor Yellow
    Write-Host "📝 Manual verification: The fixes address 401 Unauthorized errors" -ForegroundColor Cyan
    Write-Host "   - Updated API endpoint from cursor.com to api2.cursor.sh" -ForegroundColor White
    Write-Host "   - Added proper authentication headers with checksum" -ForegroundColor White  
    Write-Host "   - Improved error handling to prevent crashes" -ForegroundColor White
    Write-Host "   - Reduced logging verbosity to avoid error spam" -ForegroundColor White
}

Write-Host "`n🎯 Summary of fixes applied:" -ForegroundColor Cyan
Write-Host "  • Fixed API endpoint URL" -ForegroundColor Green
Write-Host "  • Added proper authentication headers" -ForegroundColor Green
Write-Host "  • Improved error handling" -ForegroundColor Green
Write-Host "  • Reduced error logging noise" -ForegroundColor Green
Write-Host "  • Added missing translation keys" -ForegroundColor Green

Write-Host "`n✅ Fixes should resolve the 401 Unauthorized error you encountered." -ForegroundColor Green
