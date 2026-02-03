# Deploy FIX$ to Vercel

Follow these steps to deploy your application to Vercel:

## Prerequisites

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

## Deployment Steps

### Option 1: Deploy via CLI (Recommended)

```bash
# Navigate to project directory
cd c:\FIX$APP

# Deploy to Vercel
vercel

# Follow the prompts:
# - Set up and deploy? Y
# - Which scope? (select your account)
# - Link to existing project? N (first time) or Y (if updating)
# - Project name? fix-app (or your preferred name)
# - Directory? ./ (current directory)
# - Override settings? N

# For production deployment:
vercel --prod
```

### Option 2: Deploy via Vercel Dashboard

1. Go to https://vercel.com/new
2. Import your Git repository (GitHub, GitLab, Bitbucket)
3. Configure project:
   - **Framework Preset:** Other
   - **Root Directory:** ./
   - **Build Command:** (leave empty)
   - **Output Directory:** public
4. Click "Deploy"

## Environment Variables (Optional)

If you need environment variables, add them in Vercel dashboard:

```
Settings → Environment Variables → Add
```

Common variables:
- `PYTHON_VERSION=3.11`
- `VERCEL=1` (auto-set by Vercel)

## Verify Deployment

After deployment, Vercel will provide a URL like:
```
https://fix-app-xxxxx.vercel.app
```

Test your endpoints:
```bash
# Health check
curl https://your-app.vercel.app/api/health

# Get simplified EJV
curl "https://your-app.vercel.app/api/ejv/simple/supermarket_101?zip=10001"

# View frontend
open https://your-app.vercel.app
```

## Files Configured for Vercel

✅ `vercel.json` - Vercel configuration
✅ `requirements.txt` - Python dependencies
✅ `api/index.py` - Serverless API handler (updated with simplified EJV)
✅ `database.py` - In-memory database for serverless
✅ `public/` - Static frontend files

## Project Structure

```
c:\FIX$APP/
├── vercel.json           # Vercel configuration
├── requirements.txt      # Python dependencies
├── api/
│   └── index.py         # Main API (serverless)
├── public/
│   ├── index.html       # Frontend
│   └── login-simple.html
└── database.py          # Database utilities
```

## Important Notes

### Serverless Limitations
- **In-memory database:** Data resets between invocations
- **10-second timeout:** Requests must complete within 10 seconds
- **50MB deployment size:** Keep dependencies minimal
- **Cold starts:** First request may be slower

### Optimizations Applied
- In-memory SQLite database for serverless
- Persistent connection reuse
- Minimal dependencies in requirements.txt
- Static file caching via Vercel CDN

## Troubleshooting

### Build Errors
```bash
# Check build logs
vercel logs

# Test locally
vercel dev
```

### API Not Working
- Verify `api/index.py` exports `app` variable
- Check Python version compatibility (3.9-3.11)
- Review function timeout settings

### Database Issues
- Database is ephemeral in serverless
- Consider using Vercel Postgres or external DB for persistence
- Demo user is recreated on each cold start

## Update Deployment

```bash
# Make changes to your code
# Then redeploy:
vercel --prod
```

## Custom Domain (Optional)

1. Go to Vercel Dashboard → Your Project → Settings → Domains
2. Add your custom domain
3. Configure DNS records as instructed

## Monitoring

- **Analytics:** Vercel Dashboard → Analytics
- **Logs:** `vercel logs` or Dashboard → Deployments → View Logs
- **Performance:** Dashboard shows response times and errors

## Cost

- **Hobby Plan:** FREE
  - 100GB bandwidth/month
  - Unlimited serverless function executions
  - Community support

- **Pro Plan:** $20/month (if you need more)

## Quick Deploy Command

For quick updates after code changes:

```bash
cd c:\FIX$APP
git add .
git commit -m "Update EJV calculation"
git push
# Vercel auto-deploys if connected to Git
```

---

## 🚀 Ready to Deploy!

Run this command to deploy now:

```bash
cd c:\FIX$APP
vercel --prod
```

Your app will be live in ~30 seconds! 🎉
