from django.shortcuts import render
from .models import AboutInfo, ResultInfo, ContactInfo

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
