import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from django.urls import reverse
from school.models import SchoolProfile
from achievements.models import Achievement
from ranks.models import Rank

def test_image_urls():
    """Test that all image URLs are correctly generated"""
    client = Client(HTTP_HOST='localhost')

    print("🧪 Testing Image Loading Functionality")
    print("=" * 50)

    # Test 1: Home page image URLs
    print("\n1. Testing Home Page Image URLs:")
    response = client.get('/')
    if response.status_code == 200:
        content = response.content.decode('utf-8')

        # Check for logo image
        if 'img src=' in content:
            print("✅ Home page contains image tags")

            # Check specific logo URL
            if '/media/school_logo/' in content or '/media/logos/' in content:
                print("✅ Logo URL found in home page")
            else:
                print("❌ Logo URL not found in home page")

            # Check for banner image
            if 'school_banner.jpg' in content:
                print("✅ Banner image reference found")
            else:
                print("❌ Banner image reference not found")
        else:
            print("❌ No image tags found in home page")
    else:
        print(f"❌ Home page returned status {response.status_code}")

    # Test 2: School Profile
    print("\n2. Testing School Profile:")
    profile = SchoolProfile.objects.first()
    if profile:
        print(f"✅ School profile exists: {profile.school_name}")
        if profile.logo:
            print(f"✅ Logo field: {profile.logo.url}")
            print(f"✅ Logo path exists: {Path(profile.logo.path).exists()}")
        else:
            print("❌ No logo uploaded")

        if profile.principal_photo:
            print(f"✅ Principal photo: {profile.principal_photo.url}")
        if profile.correspondent_photo:
            print(f"✅ Correspondent photo: {profile.correspondent_photo.url}")
    else:
        print("❌ No school profile found")

    # Test 3: Achievements page
    print("\n3. Testing Achievements Page:")
    response = client.get('/achievements/')
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        if 'img src=' in content:
            print("✅ Achievements page contains image tags")
            if '/media/achievements/' in content:
                print("✅ Achievement image URLs found")
            else:
                print("❌ Achievement image URLs not found")
        else:
            print("❌ No image tags in achievements page")
    else:
        print(f"❌ Achievements page returned status {response.status_code}")

    # Test 4: Ranks page
    print("\n4. Testing Ranks Page:")
    response = client.get('/ranks/')
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        if 'img src=' in content:
            print("✅ Ranks page contains image tags")
            if '/media/rank_photos/' in content or '/static/images/default_profile.png' in content:
                print("✅ Rank image URLs found")
            else:
                print("❌ Rank image URLs not found")
        else:
            print("❌ No image tags in ranks page")
    else:
        print(f"❌ Ranks page returned status {response.status_code}")

    # Test 5: Admin Portal
    print("\n5. Testing Admin Portal:")
    response = client.get('/admin_portal/school_profile/')
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        if 'img src=' in content:
            print("✅ Admin portal contains image tags")
        else:
            print("❌ No image tags in admin portal")
    else:
        print(f"❌ Admin portal returned status {response.status_code}")

    # Test 6: Check actual image files exist
    print("\n6. Checking Media Files Existence:")
    media_dir = Path('media')
    if media_dir.exists():
        print("✅ Media directory exists")

        # Check school logo
        school_logo_dir = media_dir / 'school_logo'
        if school_logo_dir.exists():
            logos = list(school_logo_dir.glob('*'))
            print(f"✅ School logo directory has {len(logos)} files: {[f.name for f in logos]}")
        else:
            print("❌ School logo directory not found")

        # Check achievements
        achievements_dir = media_dir / 'achievements'
        if achievements_dir.exists():
            ach_files = list(achievements_dir.glob('*'))
            print(f"✅ Achievements directory has {len(ach_files)} files")
        else:
            print("❌ Achievements directory not found")

        # Check profiles
        profiles_dir = media_dir / 'profiles'
        if profiles_dir.exists():
            prof_files = list(profiles_dir.glob('*'))
            print(f"✅ Profiles directory has {len(prof_files)} files")
        else:
            print("❌ Profiles directory not found")
    else:
        print("❌ Media directory not found")

    # Test 7: Static files
    print("\n7. Checking Static Files:")
    static_dir = Path('static')
    if static_dir.exists():
        images_dir = static_dir / 'images'
        if images_dir.exists():
            static_images = list(images_dir.glob('*'))
            print(f"✅ Static images directory has {len(static_images)} files: {[f.name for f in static_images]}")
        else:
            print("❌ Static images directory not found")
    else:
        print("❌ Static directory not found")

    print("\n" + "=" * 50)
    print("🧪 Image Loading Test Complete")
    print("If all checks are ✅, images should load correctly after deployment.")

if __name__ == '__main__':
    test_image_urls()
