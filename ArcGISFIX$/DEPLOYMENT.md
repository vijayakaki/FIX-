# Deployment Instructions for Vercel

## Prerequisites
- GitHub account
- Vercel account (free tier works)
- Git installed locally

## Step-by-Step Deployment

### 1. Initialize Git Repository
```powershell
cd 'c:\FIX$APP\ArcGISFIX$'
git init
git add .
git commit -m "Initial commit - FIX$ ArcGIS App"
```

### 2. Create GitHub Repository
1. Go to https://github.com/new
2. Name: `fixapp-arcgis`
3. Keep it public or private
4. Don't initialize with README (we have one)
5. Click "Create repository"

### 3. Push to GitHub
```powershell
git remote add origin https://github.com/YOUR_USERNAME/fixapp-arcgis.git
git branch -M main
git push -u origin main
```

### 4. Deploy to Vercel

#### Option A: Vercel Dashboard (Easiest)
1. Go to https://vercel.com
2. Sign in with GitHub
3. Click "Add New" → "Project"
4. Import your `fixapp-arcgis` repository
5. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: ./
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)
6. Click "Deploy"
7. Wait 1-2 minutes for deployment

#### Option B: Vercel CLI
```powershell
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
cd 'c:\FIX$APP\ArcGISFIX$'
vercel

# Follow prompts:
# - Set up and deploy? Y
# - Which scope? (your account)
# - Link to existing project? N
# - Project name? fixapp-arcgis
# - Directory? ./
# - Override settings? N

# Production deployment
vercel --prod
```

### 5. Access Your App
After deployment, Vercel provides:
- **Preview URL**: https://fixapp-arcgis-xxx.vercel.app
- **Production URL**: https://fixapp-arcgis.vercel.app

### 6. Configure Environment Variables (Optional)
In Vercel Dashboard:
1. Go to your project
2. Settings → Environment Variables
3. Add any needed variables:
   - `FLASK_ENV`: production
   - `SECRET_KEY`: your-secret-key

---

## Important Notes

### Database
⚠️ **SQLite won't work on Vercel** (read-only filesystem)

**Options:**
1. **Use Vercel Postgres** (Recommended)
   - Free tier available
   - Add in Vercel Dashboard → Storage
   
2. **Use external database**
   - PlanetScale (MySQL)
   - Supabase (PostgreSQL)
   - MongoDB Atlas

3. **For demo/testing**
   - Current app will work but data won't persist between deploys
   - Good for showcasing features

### Files Not Needed in Production
Already in `.gitignore`:
- `__pycache__/`
- `*.pyc`
- `*.db`
- `.env`
- `venv/`

---

## Updating Your Deployment

### After making changes:
```powershell
git add .
git commit -m "Description of changes"
git push origin main
```

Vercel automatically redeploys on push to main branch!

---

## Troubleshooting

### Build Fails
- Check `vercel.json` is present
- Verify `api/index.py` exists
- Check `api/requirements.txt` has all dependencies

### Import Errors
- Ensure all files are in correct structure
- Check paths in `api/index.py`

### 500 Server Error
- Check Vercel function logs in dashboard
- Look for Python errors
- Verify all imports work

### Database Issues
- Remember: SQLite won't persist on Vercel
- Use external database or accept non-persistent data

---

## Custom Domain (Optional)

1. Go to Vercel Dashboard
2. Project Settings → Domains
3. Add your domain
4. Follow DNS configuration steps
5. SSL automatically configured

---

## Monitoring

Vercel provides:
- **Real-time logs**: Dashboard → Logs
- **Analytics**: Dashboard → Analytics
- **Performance**: Response times, errors
- **Usage**: Function invocations, bandwidth

---

## Cost

**Free Tier Includes:**
- Unlimited deployments
- 100 GB bandwidth/month
- Serverless function execution
- Automatic HTTPS
- Preview deployments

Perfect for demo and small-scale production!

---

## Alternative: Persistent Database Setup

If you need persistent data, after deploying:

### Add Vercel Postgres
```powershell
# In your project directory
vercel env add DATABASE_URL
# Paste your database URL

# Update app.py to use PostgreSQL instead of SQLite
```

Or use external service:
- **Supabase**: https://supabase.com (Free tier)
- **PlanetScale**: https://planetscale.com (Free tier)
- **Neon**: https://neon.tech (Free tier)

---

## Support

- **Vercel Docs**: https://vercel.com/docs
- **Community**: https://github.com/vercel/vercel/discussions
- **Status**: https://vercel-status.com

---

**Your app will be live at: `https://fixapp-arcgis.vercel.app`** 🚀
