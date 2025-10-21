# 🚨 RAILWAY DEPLOYMENT TROUBLESHOOTING

## Current Status: Build Success, Healthcheck Failure

Your Django app is building successfully but failing the healthcheck. Here's how to fix it:

---

## 🔧 STEP-BY-STEP FIX

### **Step 1: Set Environment Variables in Railway**

Go to Railway dashboard → Your project → Variables tab and add:

```
SECRET_KEY=r(c6#w+f358j^2kurwv#t49dr@y3(!=9pq5^i^16%o7qnv_*25
DJANGO_SETTINGS_MODULE=config.settings_debug
RAILWAY_ENVIRONMENT=production
DEBUG=True
```

**Note**: Using `settings_debug` for now to help troubleshoot

### **Step 2: Add Database (if not done)**

1. In Railway dashboard, click "New"
2. Select "Database" → "PostgreSQL"
3. Wait for database to be created

### **Step 3: Redeploy**

1. Go to Railway dashboard
2. Click "Deploy" (or it will auto-redeploy)
3. Wait for deployment to complete

### **Step 4: Check Healthcheck**

After deployment, visit: `https://your-app.railway.app/health/`

This will show you:
- ✅ Environment variables status
- ✅ Database connection status
- ✅ Any configuration issues

---

## 🔍 DEBUGGING STEPS

### **Check Railway Logs**

1. Go to Railway dashboard
2. Click on your project
3. Go to "Deployments"
4. Click "View Logs"
5. Look for error messages

### **Common Error Messages & Solutions**

**Error: `SECRET_KEY not set`**
- Solution: Add SECRET_KEY environment variable

**Error: `Database connection failed`**
- Solution: Add PostgreSQL database in Railway

**Error: `No module named 'config'`**
- Solution: Check DJANGO_SETTINGS_MODULE is set correctly

**Error: `Template not found`**
- Solution: Check if templates exist in templates/ directory

**Error: `Static files not found`**
- Solution: Run `python manage.py collectstatic --noinput`

### **Test Healthcheck Endpoint**

Visit: `https://your-app.railway.app/health/`

Expected response:
```json
{
  "status": "healthy",
  "message": "Smart Schooling System is running",
  "environment": {
    "DEBUG": "True",
    "DJANGO_SETTINGS_MODULE": "config.settings_debug",
    "RAILWAY_ENVIRONMENT": "production",
    "SECRET_KEY_SET": "Yes",
    "DATABASE_URL_SET": "Yes"
  }
}
```

---

## 🚀 ALTERNATIVE DEPLOYMENT METHODS

### **Method 1: Use Debug Settings (Recommended for now)**

Environment variables:
```
SECRET_KEY=r(c6#w+f358j^2kurwv#t49dr@y3(!=9pq5^i^16%o7qnv_*25
DJANGO_SETTINGS_MODULE=config.settings_debug
RAILWAY_ENVIRONMENT=production
DEBUG=True
```

### **Method 2: Use Production Settings (After debug works)**

Environment variables:
```
SECRET_KEY=r(c6#w+f358j^2kurwv#t49dr@y3(!=9pq5^i^16%o7qnv_*25
DJANGO_SETTINGS_MODULE=config.settings_production
RAILWAY_ENVIRONMENT=production
DEBUG=False
```

---

## 📋 TROUBLESHOOTING CHECKLIST

- [ ] Environment variables set in Railway
- [ ] PostgreSQL database added
- [ ] Healthcheck endpoint accessible at `/health/`
- [ ] Railway logs checked for errors
- [ ] Database migrations run (if needed)
- [ ] Static files collected (if needed)

---

## 🆘 STILL HAVING ISSUES?

### **Check These Common Problems:**

1. **Missing Environment Variables**
   - Go to Railway dashboard → Variables
   - Add all required variables

2. **Database Not Connected**
   - Add PostgreSQL database
   - Check DATABASE_URL is set

3. **Template Issues**
   - Check if templates exist
   - Verify template paths

4. **Static Files Issues**
   - Run collectstatic command
   - Check static file configuration

### **Get Help:**

1. **Check Railway logs** for specific error messages
2. **Visit healthcheck endpoint** to see system status
3. **Test locally** with `python manage.py runserver`
4. **Share error messages** for specific help

---

## 🎯 EXPECTED RESULT

After fixing the issues:
1. ✅ Build succeeds (already working)
2. ✅ Healthcheck passes
3. ✅ App accessible at Railway URL
4. ✅ Healthcheck endpoint shows system status
5. ✅ Django admin works
6. ✅ All features functional

---

## 🚨 QUICK FIX

**Most likely solution:**
1. Set environment variables in Railway dashboard
2. Add PostgreSQL database
3. Redeploy
4. Check `/health/` endpoint

**Your app should work after these steps!**
