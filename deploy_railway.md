# 🚀 Railway Deployment Guide - UPDATED

## Prerequisites
1. GitHub account
2. Railway account (free at railway.app)
3. Your project code (already prepared!)

## Step 1: Your Code is Ready! ✅

### 1.1 Production settings are configured
- ✅ `settings_production.py` - Production-ready configuration
- ✅ `requirements_production.txt` - All dependencies included
- ✅ `railway.json` - Railway-specific configuration
- ✅ `Procfile` - Process configuration

### 1.2 Environment variables will be set in Railway dashboard
No need for local .env file - Railway handles this automatically!

## Step 2: Deploy to Railway

### 2.1 Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit for Railway deployment"
git branch -M main
git remote add origin https://github.com/yourusername/smart-schooling-system.git
git push -u origin main
```

### 2.2 Connect to Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will auto-detect Django

### 2.3 Configure Environment Variables
In Railway dashboard, go to Variables tab and add:
```
SECRET_KEY=r(c6#w+f358j^2kurwv#t49dr@y3(!=9pq5^i^16%o7qnv_*25
DJANGO_SETTINGS_MODULE=config.settings_production
RAILWAY_ENVIRONMENT=production
DEBUG=False
```

### 2.4 Add PostgreSQL Database
1. In Railway dashboard, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway will automatically set DATABASE_URL

### 2.5 Deploy
Railway will automatically:
- Install dependencies from requirements_production.txt
- Run migrations
- Start your app

## Step 3: Access Your App
Your app will be available at: `https://your-app-name.railway.app`

## Step 4: Create Superuser
```bash
# In Railway dashboard, go to Deployments → View Logs → Open Shell
python manage.py createsuperuser
```

## Troubleshooting
- Check logs in Railway dashboard
- Ensure all environment variables are set
- Verify database connection
- Check static files are being served correctly
