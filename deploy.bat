@echo off
echo ========================================
echo   FIX$ App - Vercel Deployment
echo ========================================
echo.

echo Checking Vercel CLI installation...
where vercel >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Vercel CLI not found!
    echo.
    echo Please install Vercel CLI first:
    echo   npm install -g vercel
    echo.
    pause
    exit /b 1
)

echo Vercel CLI found!
echo.

echo Deploying to Vercel...
echo.
echo TIP: For production deployment, use: vercel --prod
echo.

vercel

echo.
echo ========================================
echo   Deployment Complete!
echo ========================================
echo.
echo Your app should now be live at the URL shown above.
echo.
echo To deploy to production:
echo   vercel --prod
echo.
pause
