# 🚀 Heroku Deployment Guide

## Prerequisites
1. Heroku account (free at heroku.com)
2. Heroku CLI installed
3. Git installed

## Step 1: Install Heroku CLI
```bash
# Windows (using Chocolatey)
choco install heroku-cli

# Or download from: https://devcenter.heroku.com/articles/heroku-cli
```

## Step 2: Login to Heroku
```bash
heroku login
```

## Step 3: Create Heroku App
```bash
# Navigate to your backend directory
cd backend

# Create Heroku app
heroku create your-smart-schooling-system

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev
```

## Step 4: Configure Environment Variables
```bash
# Set secret key
heroku config:set SECRET_KEY="your-super-secret-key-here"

# Set Django settings
heroku config:set DJANGO_SETTINGS_MODULE=config.settings_production

# Set allowed hosts
heroku config:set ALLOWED_HOSTS="your-smart-schooling-system.herokuapp.com"
```

## Step 5: Deploy
```bash
# Add all files
git add .

# Commit changes
git commit -m "Deploy to Heroku"

# Deploy to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Collect static files
heroku run python manage.py collectstatic --noinput
```

## Step 6: Open Your App
```bash
heroku open
```

## Step 7: Monitor Your App
```bash
# View logs
heroku logs --tail

# Check app status
heroku ps
```

## Troubleshooting
- Check `heroku logs --tail` for errors
- Ensure Procfile is in root directory
- Verify all environment variables are set
- Check database connection with `heroku run python manage.py dbshell`
