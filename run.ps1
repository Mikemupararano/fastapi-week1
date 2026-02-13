param(
  [Parameter(Mandatory=$true)]
  [string]$App,
  [int]$Port = 8000
)

$target = Join-Path $PSScriptRoot $App

if (-not (Test-Path $target)) {
  Write-Host "❌ Folder not found: $target"
  Write-Host "Try: .\run.ps1 -App week1-fastapi -Port 8001"
  exit 1
}

Push-Location $target

if (Test-Path ".\requirements.txt") {
  python -m pip install -r .\requirements.txt
}

python -m uvicorn main:app --reload --port $Port

Pop-Location
