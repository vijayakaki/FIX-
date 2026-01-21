# 🚀 Quick Deploy to Vercel

## Instant Deploy (3 Steps)

### 1️⃣ Run Deploy Script
```powershell
cd 'c:\FIX$APP\ArcGISFIX$'
.\deploy.ps1
```

### 2️⃣ Create GitHub Repo
- Go to: https://github.com/new
- Name: `fixapp-arcgis`
- Click "Create repository"
- Copy the URL

### 3️⃣ Deploy on Vercel
- Go to: https://vercel.com
- Click "Add New" → "Project"
- Import your GitHub repo
- Click "Deploy"

**Done! Live in 2 minutes** ✨

---

## Manual Deploy (If Script Fails)

```powershell
# Initialize Git
cd 'c:\FIX$APP\ArcGISFIX$'
git init
git add .
git commit -m "Initial deploy"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/fixapp-arcgis.git
git branch -M main
git push -u origin main

# Then deploy on Vercel dashboard
```

---

## Files Created for Vercel

✅ `vercel.json` - Configuration
✅ `api/index.py` - Serverless entry point
✅ `api/requirements.txt` - Dependencies
✅ `.gitignore` - Updated
✅ `deploy.ps1` - Deploy helper script

---

## After Deployment

Your app will be live at:
```
https://fixapp-arcgis.vercel.app
```

Or custom domain:
```
https://your-domain.com
```

---

## Important Notes

⚠️ **Database**: SQLite won't persist on Vercel
- Works for demo/testing
- For production: Use Vercel Postgres or external DB

✅ **Auto-deploys**: Every push to `main` branch deploys automatically

✅ **Free Tier**: Includes everything you need for this app

---

## Update App Later

```powershell
git add .
git commit -m "Your changes"
git push origin main
```

Vercel redeploys automatically!

---

## Get Help

- Full guide: [DEPLOYMENT.md](DEPLOYMENT.md)
- Vercel docs: https://vercel.com/docs
- Issues: Check Vercel dashboard logs
