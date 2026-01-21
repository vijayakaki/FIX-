# Quick Deploy Script for Vercel

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "FIX$ ArcGIS - Vercel Deployment Helper" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is initialized
if (-not (Test-Path .git)) {
    Write-Host "Initializing Git repository..." -ForegroundColor Yellow
    git init
    Write-Host "✓ Git initialized" -ForegroundColor Green
}

# Add all files
Write-Host ""
Write-Host "Adding files to Git..." -ForegroundColor Yellow
git add .

# Commit
Write-Host ""
$commitMsg = Read-Host "Enter commit message (or press Enter for default)"
if ([string]::IsNullOrWhiteSpace($commitMsg)) {
    $commitMsg = "Deploy FIX$ ArcGIS App - $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
}

git commit -m $commitMsg
Write-Host "✓ Changes committed" -ForegroundColor Green

# Check if remote exists
$remotes = git remote
if ($remotes -notcontains "origin") {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host "SETUP REQUIRED" -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "1. Create a new repository on GitHub:" -ForegroundColor Cyan
    Write-Host "   https://github.com/new" -ForegroundColor White
    Write-Host ""
    Write-Host "2. Copy the repository URL" -ForegroundColor Cyan
    Write-Host ""
    $repoUrl = Read-Host "Enter your GitHub repository URL (e.g., https://github.com/username/fixapp-arcgis.git)"
    
    if (![string]::IsNullOrWhiteSpace($repoUrl)) {
        git remote add origin $repoUrl
        git branch -M main
        Write-Host "✓ Remote added" -ForegroundColor Green
    }
}

# Push to GitHub
Write-Host ""
Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
try {
    git push -u origin main
    Write-Host "✓ Pushed to GitHub" -ForegroundColor Green
} catch {
    Write-Host "⚠ Push failed. You may need to authenticate." -ForegroundColor Red
    Write-Host "Run manually: git push -u origin main" -ForegroundColor Yellow
}

# Vercel deployment instructions
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "NEXT STEPS - Deploy to Vercel" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Option 1: Vercel Dashboard (Easiest)" -ForegroundColor Yellow
Write-Host "1. Go to: https://vercel.com" -ForegroundColor White
Write-Host "2. Sign in with GitHub" -ForegroundColor White
Write-Host "3. Click 'Add New' → 'Project'" -ForegroundColor White
Write-Host "4. Import your 'fixapp-arcgis' repository" -ForegroundColor White
Write-Host "5. Click 'Deploy' (use default settings)" -ForegroundColor White
Write-Host ""
Write-Host "Option 2: Vercel CLI" -ForegroundColor Yellow
Write-Host "1. Install: npm install -g vercel" -ForegroundColor White
Write-Host "2. Login: vercel login" -ForegroundColor White
Write-Host "3. Deploy: vercel --prod" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Your app will be live in 1-2 minutes!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "⚠ Note: SQLite database won't persist on Vercel" -ForegroundColor Yellow
Write-Host "   Use Vercel Postgres or external DB for production" -ForegroundColor Yellow
Write-Host ""
