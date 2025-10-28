# 🚀 Render Deployment Guide - Smart Schooling System

## Prerequisites
- ✅ GitHub account
- ✅ Render account (free at render.com)
- ✅ Your PostgreSQL database (already created)

## Step 1: Push Code to GitHub

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit changes
git commit -m "Ready for Render deployment with PostgreSQL"

# Create/push to GitHub repository
git branch -M main
git remote add origin https://github.com/yourusername/smart-schooling-system.git
git push -u origin main
```

## Step 2: Deploy to Render

### 2.1 Create New Web Service
1. Go to [render.com](https://render.com) and sign in
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Choose your repository: `smart-schooling-system`

### 2.2 Configure Service Settings

**Basic Settings:**
- **Name**: `smart-schooling-system` (or your preferred name)
- **Runtime**: `Python`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python manage.py migrate && python manage.py createsuperuser --noinput --username Harsha@108 --email harsha@school.com || true && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT`

**Environment Variables:**
Add these environment variables in Render dashboard:

```
DJANGO_SETTINGS_MODULE=config.settings_production
PYTHON_VERSION=3.11.0
DJANGO_SUPERUSER_PASSWORD=admin123
SECRET_KEY=your-super-secret-key-here-generate-a-long-random-one
RENDER=true
DATABASE_URL=postgresql://deeptihome_user:30u9m67dN95DoisgtDLn4bvbBtH7khNy@dpg-d3vpoo49c44c738q3c8g-a.oregon-postgres.render.com/deeptihome
```

**Advanced Settings:**
- **Health Check Path**: `/health/`
- **Instance Type**: Free tier (or upgrade as needed)

### 2.3 Deploy
1. Click **"Create Web Service"**
2. Render will automatically:
   - Install dependencies
   - Run database migrations
   - Create superuser
   - Collect static files
   - Start the application

## Step 3: Access Your Application

Once deployment is complete, your app will be available at:
```
https://your-service-name.onrender.com
```

## Step 4: Verify Deployment

### Check Health Endpoint
Visit: `https://your-service-name.onrender.com/health/`

Expected response:
```json
{
  "status": "healthy",
  "message": "Smart Schooling System is running",
  "environment": {
    "DEBUG": "False",
    "DJANGO_SETTINGS_MODULE": "config.settings_production",
    "RENDER": "true",
    "SECRET_KEY_SET": "Yes",
    "DATABASE_URL_SET": "Yes"
  }
}
```

### Access Admin Panel
1. Go to: `https://your-service-name.onrender.com/admin/`
2. Login with:
   - **Username**: `Harsha@108`
   - **Password**: `admin123`

## Step 5: Troubleshooting

### Common Issues

**1. Database Connection Failed**
- Verify `DATABASE_URL` is correctly set
- Check PostgreSQL credentials are valid
- Ensure database allows external connections

**2. Static Files Not Loading**
- Check that `collectstatic` ran successfully in logs
- Verify static files are in the correct directory

**3. Application Won't Start**
- Check deployment logs in Render dashboard
- Verify all environment variables are set
- Ensure Python version compatibility

**4. Health Check Failing**
- Check `/health/` endpoint response
- Verify database connectivity
- Check application logs

### Viewing Logs
1. Go to your Render service dashboard
2. Click **"Logs"** tab
3. Check for error messages

### Environment Variables Check
In Render dashboard → Environment:
- All required variables should be set
- `SECRET_KEY` should be long and random
- `DATABASE_URL` should match your PostgreSQL instance

## Step 6: Post-Deployment Tasks

### 1. Update ALLOWED_HOSTS (if needed)
If your domain is different, update `config/settings_production.py`:
```python
ALLOWED_HOSTS = [
    'your-actual-domain.onrender.com',
    'localhost',
    '127.0.0.1',
]
```

### 2. Configure Custom Domain (Optional)
- Go to Render dashboard → Settings → Custom Domains
- Add your custom domain
- Update DNS records as instructed

### 3. Set Up Monitoring (Recommended)
- Enable health checks
- Set up alerts for downtime
- Monitor resource usage

## Step 7: Production Security

### Generate Strong SECRET_KEY
```python
# Run this in Python shell to generate a secure key
import secrets
print(secrets.token_urlsafe(50))
```

### Update Superuser Password
After first login, change the default admin password:
1. Login to admin panel
2. Go to Users → Harsha@108
3. Change password to something secure

## 📞 Support

If you encounter issues:
1. Check Render deployment logs
2. Verify environment variables
3. Test database connectivity locally
4. Review Django settings configuration

Your Smart Schooling System is now ready for production! 🎉
