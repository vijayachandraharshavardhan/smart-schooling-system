from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import ClassSection, Attendance, Homework, Exam, Performance, Teacher, Subject
from student.models import Student


# -------------------------------
# TEACHER LOGIN
# -------------------------------
def teacher_login(request):
    if request.user.is_authenticated and hasattr(request.user, 'teacher_profile'):
        return redirect('teacher:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and hasattr(user, 'teacher_profile'):
            login(request, user)
            messages.success(request, f"Welcome, {user.teacher_profile.name}!")
            return redirect('teacher:dashboard')
        else:
            messages.error(request, "Invalid teacher credentials.")
    return render(request, 'teacher/teacher_login.html')


# -------------------------------
# TEACHER LOGOUT
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def teacher_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('/users/login/teacher/')


# -------------------------------
# DASHBOARD
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def dashboard(request):
    teacher = request.user.teacher_profile
    classes = ClassSection.objects.all()
    return render(request, 'teacher/dashboard.html', {'classes': classes, 'teacher': teacher})


# -------------------------------
# ATTENDANCE
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def attendance(request):
    teacher = request.user.teacher_profile
    classes = ClassSection.objects.all()
    selected_class = None
    students = []
    today = timezone.now().date()

    class_id = request.GET.get('class_id')
    if class_id:
        selected_class = get_object_or_404(ClassSection, id=class_id)
        students = Student.objects.filter(student_class=selected_class).order_by('roll_number')

    if request.method == 'POST' and selected_class:
        date_str = request.POST.get('date')
        date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else today

        for student in students:
            status = request.POST.get(f'status_{student.id}', 'Absent')
            Attendance.objects.update_or_create(
                class_section=selected_class,
                student=student,
                subject=teacher.subject,
                date=date,
                defaults={'status': status, 'teacher': teacher}
            )
        messages.success(request, f"✅ Attendance saved for {selected_class} on {date}.")
        return redirect(f'/teacher/attendance/?class_id={selected_class.id}')

    context = {
        'classes': classes,
        'selected_class': selected_class,
        'students': students,
        'today': today,
        'subject': teacher.subject
    }
    return render(request, 'teacher/attendance.html', context)


# -------------------------------
# HOMEWORK
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def homework(request):
    teacher = request.user.teacher_profile
    classes = ClassSection.objects.all()
    subjects = Subject.objects.all()
    homeworks = Homework.objects.all().order_by('-updated_at')

    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        subject_id = request.POST.get('subject')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        if not all([class_id, subject_id, description, due_date]):
            messages.error(request, "⚠️ All fields are required.")
        else:
            Homework.objects.create(
                class_section_id=class_id,
                subject_id=subject_id,
                description=description,
                due_date=due_date
            )
            messages.success(request, "✅ Homework added successfully!")
            return redirect('teacher:homework')

    context = {
        'classes': classes,
        'subjects': subjects,
        'teacher': teacher,
        'homeworks': homeworks
    }
    return render(request, 'teacher/homework.html', context)


# -------------------------------
# EXAMS  ✅ UPDATED
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def exams(request):
    teacher = request.user.teacher_profile
    classes = ClassSection.objects.all()
    subjects = Subject.objects.all()
    exams = Exam.objects.all().order_by('-exam_date')

    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        subject_id = request.POST.get('subject')
        exam_date = request.POST.get('exam_date')
        max_marks = request.POST.get('max_marks')
        syllabus = request.POST.get('syllabus')

        if not all([class_id, subject_id, exam_date, max_marks]):
            messages.error(request, "⚠️ All fields are required.")
        else:
            Exam.objects.create(
                class_section_id=class_id,
                subject_id=subject_id,
                exam_date=exam_date,
                max_marks=max_marks,
                syllabus=syllabus
            )
            messages.success(request, "✅ Exam details saved successfully!")
            return redirect('teacher:exams')

    return render(request, 'teacher/exams.html', {
        'classes': classes,
        'subjects': subjects,
        'teacher': teacher,
        'exams': exams
    })


# -------------------------------
# PERFORMANCE
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def performance(request):
    teacher = request.user.teacher_profile
    classes = ClassSection.objects.all()
    subjects = Subject.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        class_id = request.POST.get('class_id')
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        marks = request.POST.get('marks')
        remarks = request.POST.get('remarks', '')

        if not all([class_id, student_id, subject_id, marks]):
            messages.error(request, "⚠️ All fields are required.")
        else:
            Performance.objects.update_or_create(
                class_section_id=class_id,
                student_id=student_id,
                subject_id=subject_id,
                defaults={'marks': marks, 'remarks': remarks}
            )
            messages.success(request, "✅ Performance saved successfully!")
            return redirect('teacher:performance')

    return render(request, 'teacher/performance.html', {
        'classes': classes,
        'subjects': subjects,
        'students': students,
        'teacher': teacher
    })
