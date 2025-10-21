# 🚀 DigitalOcean VPS Deployment Guide

## Prerequisites
1. DigitalOcean account
2. Domain name (optional)
3. SSH client

## Step 1: Create Droplet
1. Go to DigitalOcean dashboard
2. Click "Create" → "Droplets"
3. Choose Ubuntu 22.04 LTS
4. Select Basic plan ($6/month minimum)
5. Add SSH key or use password
6. Create droplet

## Step 2: Connect to Server
```bash
# Connect via SSH
ssh root@your-server-ip

# Update system
apt update && apt upgrade -y
```

## Step 3: Install Dependencies
```bash
# Install Python and pip
apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib -y

# Install Node.js (for static files)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
apt install nodejs -y
```

## Step 4: Setup Database
```bash
# Switch to postgres user
sudo -u postgres psql

# Create database and user
CREATE DATABASE smart_schooling;
CREATE USER school_admin WITH PASSWORD 'your_secure_password';
GRANT ALL PRIVILEGES ON DATABASE smart_schooling TO school_admin;
\q
```

## Step 5: Deploy Application
```bash
# Create application directory
mkdir -p /var/www/smart-schooling
cd /var/www/smart-schooling

# Clone your repository
git clone https://github.com/yourusername/smart-schooling-system.git .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements_production.txt

# Copy production settings
cp config/settings_production.py config/settings_production.py

# Set environment variables
export SECRET_KEY="your-super-secret-key"
export DATABASE_NAME="smart_schooling"
export DATABASE_USER="school_admin"
export DATABASE_PASSWORD="your_secure_password"
export DATABASE_HOST="localhost"
export DATABASE_PORT="5432"

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

## Step 6: Configure Gunicorn
```bash
# Create gunicorn service file
nano /etc/systemd/system/smart-schooling.service
```

Add this content:
```ini
[Unit]
Description=Smart Schooling System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/smart-schooling/backend
Environment="PATH=/var/www/smart-schooling/backend/venv/bin"
ExecStart=/var/www/smart-schooling/backend/venv/bin/gunicorn --workers 3 --bind unix:/var/www/smart-schooling/backend/smart-schooling.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
```

## Step 7: Configure Nginx
```bash
# Create nginx configuration
nano /etc/nginx/sites-available/smart-schooling
```

Add this content:
```nginx
server {
    listen 80;
    server_name your-domain.com your-server-ip;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/smart-schooling/backend;
    }
    
    location /media/ {
        root /var/www/smart-schooling/backend;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/smart-schooling/backend/smart-schooling.sock;
    }
}
```

## Step 8: Enable Services
```bash
# Enable nginx site
ln -s /etc/nginx/sites-available/smart-schooling /etc/nginx/sites-enabled
rm /etc/nginx/sites-enabled/default

# Test nginx configuration
nginx -t

# Start services
systemctl start smart-schooling
systemctl enable smart-schooling
systemctl restart nginx

# Check status
systemctl status smart-schooling
systemctl status nginx
```

## Step 9: Setup SSL (Optional)
```bash
# Install Certbot
apt install certbot python3-certbot-nginx -y

# Get SSL certificate
certbot --nginx -d your-domain.com

# Auto-renewal
crontab -e
# Add this line:
0 12 * * * /usr/bin/certbot renew --quiet
```

## Step 10: Access Your Application
Your application will be available at:
- `http://your-server-ip` (HTTP)
- `https://your-domain.com` (HTTPS with SSL)

## Troubleshooting
```bash
# Check application logs
journalctl -u smart-schooling -f

# Check nginx logs
tail -f /var/log/nginx/error.log

# Restart services
systemctl restart smart-schooling
systemctl restart nginx
```
