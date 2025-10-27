from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse

# -------------------------------
# TEACHER LOGIN
# -------------------------------
def login_teacher(request):
    if request.user.is_authenticated:
        return redirect('teacher:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  # Assuming teachers are staff
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('teacher:dashboard')
        else:
            messages.error(request, "Invalid teacher credentials.")

    return render(request, 'teacher/teacher_login.html')


# -------------------------------
# ADMIN LOGIN (optional)
# -------------------------------
def login_admin(request):
    if request.user.is_authenticated:
        return redirect('/admin/')  # Default Django admin

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/admin/')
        else:
            messages.error(request, "Invalid admin credentials.")

    return render(request, 'users/admin_login.html')
