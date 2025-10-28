from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AboutInfo, ResultInfo, ContactInfo
from school.models import SchoolProfile
from django.core.files.storage import default_storage

# -------------------------
# Home Page
# -------------------------
def home_view(request):
    """
    Renders the home page.
    """
    return render(request, "admin_portal/home.html")


# -------------------------
# About Page
# -------------------------
def about_view(request):
    """
    Fetches the latest About information added by admin and displays it.
    If no About entry exists, passes None to the template.
    """
    about_entry = AboutInfo.objects.order_by('-updated_at').first()  # latest entry
    return render(request, "admin_portal/about.html", {"about": about_entry})


# -------------------------
# Results Page
# -------------------------
def results_view(request):
    """
    Fetches all Results uploaded by admin and displays them, newest first.
    """
    results = ResultInfo.objects.all().order_by('-uploaded_at')
    return render(request, "admin_portal/results.html", {"results": results})


# -------------------------
# Contact Page
# -------------------------
def contact_view(request):
    """
    Fetches the latest Contact Info uploaded by admin.
    If no entry exists, passes None to the template.
    """
    contact = ContactInfo.objects.order_by('-updated_at').first()
    return render(request, "admin_portal/contact.html", {"contact": contact})


# -------------------------
# School Profile Management
# -------------------------
def school_profile_view(request):
    """
    Handles GET and POST for school profile management.
    GET: Displays the current school profile.
    POST: Updates the school profile with uploaded files.
    """
    profile = SchoolProfile.objects.first()
    if not profile:
        profile = SchoolProfile.objects.create(school_name="DEEPTI EM HIGH SCHOOL")

    if request.method == 'POST':
        # Update school name
        school_name = request.POST.get('name')
        if school_name:
            profile.school_name = school_name

        # Handle logo upload
        if 'logo' in request.FILES:
            # Delete old logo if exists
            if profile.logo:
                default_storage.delete(profile.logo.path)
            profile.logo = request.FILES['logo']

        # Handle HM photo upload
        if 'hm_photo' in request.FILES:
            if profile.principal_photo:
                default_storage.delete(profile.principal_photo.path)
            profile.principal_photo = request.FILES['hm_photo']

        # Handle correspondent photo upload
        if 'correspondent_photo' in request.FILES:
            if profile.correspondent_photo:
                default_storage.delete(profile.correspondent_photo.path)
            profile.correspondent_photo = request.FILES['correspondent_photo']

        profile.save()
        messages.success(request, "School profile updated successfully!")
        return redirect('admin_portal:school_profile')

    return render(request, "admin_portal/school_profile.html", {"profile": profile})
