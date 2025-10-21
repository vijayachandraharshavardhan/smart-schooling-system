# 🚀 AWS Deployment Guide (Advanced)

## Prerequisites
1. AWS account
2. AWS CLI installed
3. Domain name
4. Basic AWS knowledge

## Step 1: Setup AWS CLI
```bash
# Install AWS CLI
pip install awscli

# Configure AWS CLI
aws configure
# Enter your Access Key ID, Secret Access Key, and region
```

## Step 2: Create RDS Database
```bash
# Create RDS instance
aws rds create-db-instance \
    --db-instance-identifier smart-schooling-db \
    --db-instance-class db.t3.micro \
    --engine postgres \
    --master-username school_admin \
    --master-user-password your_secure_password \
    --allocated-storage 20 \
    --vpc-security-group-ids sg-xxxxxxxxx
```

## Step 3: Create S3 Bucket for Media Files
```bash
# Create S3 bucket
aws s3 mb s3://your-smart-schooling-media

# Create IAM user for S3 access
aws iam create-user --user-name smart-schooling-s3-user

# Create access key
aws iam create-access-key --user-name smart-schooling-s3-user
```

## Step 4: Deploy with Elastic Beanstalk
```bash
# Install EB CLI
pip install awsebcli

# Initialize EB application
eb init

# Create environment
eb create production

# Deploy
eb deploy
```

## Step 5: Configure Environment Variables
In AWS Elastic Beanstalk console:
```
SECRET_KEY=your-super-secret-key
DATABASE_NAME=smart_schooling
DATABASE_USER=school_admin
DATABASE_PASSWORD=your_secure_password
DATABASE_HOST=your-rds-endpoint
DATABASE_PORT=5432
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-smart-schooling-media
```

## Step 6: Setup CloudFront (Optional)
```bash
# Create CloudFront distribution for static files
aws cloudfront create-distribution \
    --distribution-config file://cloudfront-config.json
```

## Step 7: Configure Custom Domain
1. Go to Route 53
2. Create hosted zone for your domain
3. Update nameservers with your domain registrar
4. Create A record pointing to your EB environment

## Step 8: Setup Monitoring
```bash
# Enable CloudWatch monitoring
aws cloudwatch put-metric-alarm \
    --alarm-name "Smart-Schooling-High-CPU" \
    --alarm-description "High CPU usage" \
    --metric-name CPUUtilization \
    --namespace AWS/EC2 \
    --statistic Average \
    --period 300 \
    --threshold 80 \
    --comparison-operator GreaterThanThreshold
```

## Troubleshooting
- Check EB logs: `eb logs`
- Monitor CloudWatch metrics
- Check RDS connection
- Verify S3 permissions
- Test load balancer health
