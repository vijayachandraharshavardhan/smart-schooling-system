#!/bin/bash

# 🚀 Quick Deployment Script for Smart Schooling System
# Choose your deployment method by uncommenting the relevant section

echo "🚀 Smart Schooling System - Quick Deployment"
echo "============================================="
echo ""

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Please run this script from the backend directory"
    exit 1
fi

echo "📋 Available deployment options:"
echo "1. Railway (Easiest - Free)"
echo "2. Heroku (Popular - Free tier available)"
echo "3. DigitalOcean VPS (Full control - $6/month)"
echo "4. AWS (Advanced - Pay as you use)"
echo ""

read -p "Choose deployment method (1-4): " choice

case $choice in
    1)
        echo "🚀 Deploying to Railway..."
        echo "1. Go to https://railway.app"
        echo "2. Sign up with GitHub"
        echo "3. Create new project from GitHub repo"
        echo "4. Add PostgreSQL database"
        echo "5. Set environment variables:"
        echo "   - SECRET_KEY=your-secret-key"
        echo "   - DJANGO_SETTINGS_MODULE=config.settings_production"
        echo "   - RAILWAY_ENVIRONMENT=production"
        echo ""
        echo "📁 Files created for Railway:"
        echo "   ✅ settings_production.py"
        echo "   ✅ requirements_production.txt"
        echo "   ✅ railway.json"
        echo "   ✅ Procfile"
        ;;
    2)
        echo "🚀 Deploying to Heroku..."
        echo "1. Install Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli"
        echo "2. Run these commands:"
        echo ""
        echo "   heroku login"
        echo "   heroku create your-smart-schooling-system"
        echo "   heroku addons:create heroku-postgresql:hobby-dev"
        echo "   heroku config:set SECRET_KEY='your-secret-key'"
        echo "   heroku config:set DJANGO_SETTINGS_MODULE=config.settings_production"
        echo "   git push heroku main"
        echo "   heroku run python manage.py migrate"
        echo "   heroku run python manage.py createsuperuser"
        echo "   heroku run python manage.py collectstatic --noinput"
        ;;
    3)
        echo "🚀 Deploying to DigitalOcean VPS..."
        echo "1. Create Ubuntu 22.04 droplet"
        echo "2. Connect via SSH"
        echo "3. Run the setup script:"
        echo ""
        echo "   curl -sSL https://raw.githubusercontent.com/yourusername/smart-schooling-system/main/backend/setup_vps.sh | bash"
        ;;
    4)
        echo "🚀 Deploying to AWS..."
        echo "1. Setup AWS CLI and configure credentials"
        echo "2. Create RDS PostgreSQL instance"
        echo "3. Create S3 bucket for media files"
        echo "4. Deploy with Elastic Beanstalk"
        echo "5. Configure CloudFront for static files"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "📚 For detailed instructions, see:"
echo "   - deploy_railway.md (Railway)"
echo "   - deploy_heroku.md (Heroku)"
echo "   - deploy_digitalocean.md (DigitalOcean)"
echo "   - deploy_aws.md (AWS)"
echo ""
echo "✅ Deployment files created successfully!"
echo "🎉 Your Smart Schooling System is ready to deploy!"
