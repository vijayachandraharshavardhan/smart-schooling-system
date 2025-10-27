# 🚀 Step-by-Step Deployment Commands

## 🎯 RECOMMENDED: Railway Deployment (5 minutes)

### Step 1: Prepare Your Code
```bash
# Navigate to your project
cd "D:\SMART SCHOOLING SYSTEM\DEEPTI_HOME\backend"

# Initialize git (if not already done)
git init
git add .
git commit -m "Ready for Railway deployment"
```

### Step 2: Push to GitHub
```bash
# Create repository on GitHub first, then:
git remote add origin https://github.com/yourusername/smart-schooling-system.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add PostgreSQL database
6. Set environment variables:
   - `SECRET_KEY`: Generate a strong secret key
   - `DJANGO_SETTINGS_MODULE`: `config.settings_production`
   - `RAILWAY_ENVIRONMENT`: `production`

### Step 4: Access Your App
Your app will be live at: `https://your-app-name.railway.app`

---

## 🌐 Heroku Deployment (10 minutes)

### Step 1: Install Heroku CLI
```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
# Or use package manager:
# Windows: choco install heroku-cli
# Mac: brew install heroku/brew/heroku
```

### Step 2: Login and Create App
```bash
heroku login
heroku create your-smart-schooling-system
heroku addons:create heroku-postgresql:hobby-dev
```

### Step 3: Configure Environment
```bash
heroku config:set SECRET_KEY="your-super-secret-key-here"
heroku config:set DJANGO_SETTINGS_MODULE=config.settings_production
heroku config:set ALLOWED_HOSTS="your-smart-schooling-system.herokuapp.com"
```

### Step 4: Deploy
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py collectstatic --noinput
heroku open
```

---

## 🖥️ DigitalOcean VPS (15 minutes)

### Step 1: Create Droplet
1. Go to DigitalOcean dashboard
2. Create Ubuntu 22.04 droplet ($6/month)
3. Connect via SSH: `ssh root@your-server-ip`

### Step 2: Server Setup
```bash
# Update system
apt update && apt upgrade -y

# Install dependencies
apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Setup database
sudo -u postgres psql
CREATE DATABASE smart_schooling;
CREATE USER school_admin WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE smart_schooling TO school_admin;
\q
```

### Step 3: Deploy Application
```bash
# Create app directory
mkdir -p /var/www/smart-schooling
cd /var/www/smart-schooling

# Clone repository
git clone https://github.com/yourusername/smart-schooling-system.git .

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_production.txt

# Configure environment
export SECRET_KEY="your-super-secret-key"
export DATABASE_NAME="smart_schooling"
export DATABASE_USER="school_admin"
export DATABASE_PASSWORD="your_secure_password"
export DATABASE_HOST="localhost"
export DATABASE_PORT="5432"

# Setup application
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

### Step 4: Configure Services
```bash
# Create systemd service
nano /etc/systemd/system/smart-schooling.service
# (Add service configuration from deploy_digitalocean.md)

# Configure nginx
nano /etc/nginx/sites-available/smart-schooling
# (Add nginx configuration from deploy_digitalocean.md)

# Enable services
systemctl start smart-schooling
systemctl enable smart-schooling
systemctl restart nginx
```

---

## ☁️ AWS Deployment (30 minutes)

### Step 1: Setup AWS CLI
```bash
pip install awscli
aws configure
# Enter your AWS credentials
```

### Step 2: Create RDS Database
```bash
aws rds create-db-instance \
    --db-instance-identifier smart-schooling-db \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --master-username school_admin \
    --master-user-password your_secure_password \
    --allocated-storage 20
```

### Step 3: Deploy with Elastic Beanstalk
```bash
pip install awsebcli
eb init
eb create production
eb deploy
```

### Step 4: Configure Environment
In AWS EB console, set environment variables:
- `SECRET_KEY`: your secret key
- `DATABASE_NAME`: smart_schooling
- `DATABASE_USER`: school_admin
- `DATABASE_PASSWORD`: your password
- `DATABASE_HOST`: your RDS endpoint

---

## 🔧 Post-Deployment Tasks

### 1. Create Superuser
```bash
# Railway/Heroku
python manage.py createsuperuser

# VPS/AWS
python manage.py createsuperuser
```

### 2. Test Your Application
- Visit your deployed URL
- Test login functionality
- Check static files are loading
- Verify database connections

### 3. Monitor Your Application
```bash
# Railway: Check logs in dashboard
# Heroku: heroku logs --tail
# VPS: journalctl -u smart-schooling -f
# AWS: eb logs
```

### 4. Setup Custom Domain (Optional)
- Point your domain to your deployment
- Configure SSL certificates
- Update ALLOWED_HOSTS

---

## 🚨 Troubleshooting Common Issues

### Database Connection Issues
```bash
# Check database URL
echo $DATABASE_URL

# Test connection
python manage.py dbshell
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput

# Check static file configuration
python manage.py findstatic admin/css/base.css
```

### Environment Variables Not Set
```bash
# Check all environment variables
env | grep -E "(SECRET_KEY|DATABASE|DJANGO)"

# Set missing variables
export SECRET_KEY="your-secret-key"
```

### Application Not Starting
```bash
# Check application logs
# Railway: Dashboard → Deployments → View Logs
# Heroku: heroku logs --tail
# VPS: journalctl -u smart-schooling -f
```

---

## 📊 Performance Optimization

### 1. Enable Caching
```python
# In settings_production.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

### 2. Use CDN for Static Files
```python
# Configure AWS CloudFront or similar
STATIC_URL = 'https://your-cdn-domain.com/static/'
```

### 3. Database Optimization
```python
# Add database indexes
# Use connection pooling
# Enable query optimization
```

---

## 🔒 Security Checklist

- [ ] Change default SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Use HTTPS
- [ ] Enable security headers
- [ ] Regular security updates
- [ ] Database backups
- [ ] Monitor logs for suspicious activity

---

## 📈 Scaling Considerations

### For High Traffic:
1. **Database**: Upgrade to larger instance
2. **Caching**: Implement Redis/Memcached
3. **Load Balancing**: Use multiple app instances
4. **CDN**: Serve static files from CDN
5. **Monitoring**: Setup application monitoring

### Cost Optimization:
1. **Railway**: Free tier available
2. **Heroku**: $7/month for basic
3. **DigitalOcean**: $6/month for VPS
4. **AWS**: Pay-as-you-use pricing

---

## 🎉 Success!

Your Smart Schooling System is now live and accessible to users worldwide! 

**Next Steps:**
1. Test all functionality
2. Create user accounts
3. Add school data
4. Monitor performance
5. Plan for scaling
