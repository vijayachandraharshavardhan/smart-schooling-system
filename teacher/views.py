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
    import logging
    logger = logging.getLogger(__name__)
    logger.info(f"Attendance view called by user: {request.user}")

    teacher = request.user.teacher_profile
    logger.info(f"Teacher profile: {teacher}, subject: {teacher.subject}, class_section: {teacher.class_section}")

    subject = teacher.subject
    if not subject:
        logger.warning(f"Teacher {teacher} has no assigned subject")
        messages.warning(request, "You are not assigned to any subject yet!")
        return render(request, "teacher/attendance.html", {'teacher': teacher})

    students = Student.objects.filter(student_class=teacher.class_section).order_by('roll_number')
    logger.info(f"Found {students.count()} students in class {teacher.class_section}")

    today = timezone.now().date()
    logger.info(f"Today's date: {today}")

    # Load existing attendance
    attendance_data = {a.student_id: a.status for a in Attendance.objects.filter(
        subject=subject, date=today
    )}
    logger.info(f"Existing attendance data: {attendance_data}")

    if request.method == "POST":
        logger.info("Processing POST request for attendance")
        date_str = request.POST.get('date')
        logger.info(f"Date from POST: {date_str}")
        date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else today
        logger.info(f"Parsed date: {date}")

        try:
            for student in students:
                present = request.POST.get(f'present_{student.id}')
                absent = request.POST.get(f'absent_{student.id}')
                status = 'Present' if present else 'Absent' if absent else 'Absent'
                logger.info(f"Student {student.id}: present={present}, absent={absent}, status={status}")

                Attendance.objects.update_or_create(
                    student=student,
                    subject=subject,
                    date=date,
                    defaults={'status': status, 'teacher': teacher,
                              'class_section': teacher.class_section}
                )

            messages.success(request, f"✅ Attendance saved successfully for {subject.name} on {date}.")
            logger.info("Attendance saved, redirecting to teacher:attendance")
            return redirect('teacher:attendance')
        except Exception as e:
            logger.error(f"Error saving attendance: {e}")
            messages.error(request, f"❌ Error saving attendance: {str(e)}")
            return redirect('teacher:attendance')

    context = {
        'teacher': teacher,
        'subject': subject,
        'students': students,
        'attendance_data': attendance_data,
        'today': today
    }
    logger.info(f"Rendering attendance template with context: teacher={teacher}, subject={subject}, students_count={len(students)}")
    return render(request, 'teacher/attendance.html', context)


# -------------------------------
# HOMEWORK
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def homework(request):
    teacher = request.user.teacher_profile
    classes = ClassSection.objects.all()
    subjects = [teacher.subject] if teacher.subject else []
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
# EXAMS
# -------------------------------
@login_required(login_url='/users/login/teacher/')
def exams(request):
    teacher = request.user.teacher_profile
    classes = ClassSection.objects.all()
    subjects = [teacher.subject] if teacher.subject else []
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
    subjects = [teacher.subject] if teacher.subject else []
    students = Student.objects.filter(student_class=teacher.class_section).order_by('roll_number')

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
