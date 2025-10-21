from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from collections import defaultdict
from teacher.models import ClassSection, Attendance, Homework, Exam, Performance, Subject
from student.models import Student


# -------------------------------
# DASHBOARD
# -------------------------------
def dashboard(request):
    """Student dashboard — navigation hub."""
    return render(request, 'student/dashboard.html')


# -------------------------------
# ATTENDANCE VIEW
# -------------------------------
def attendance_view(request):
    """
    Display student attendance:
    - Dates as rows
    - Subjects as columns
    - Shows P (Present), A (Absent), - (no record)
    """
    student = None
    subjects = []
    attendance_matrix = defaultdict(dict)
    total_classes = present_count = attendance_percentage = 0
    sorted_dates = []

    if request.method == "POST":
        roll_number = request.POST.get("roll_number", "").strip()
        if roll_number:
            try:
                student = Student.objects.get(roll_number=roll_number)
                subjects = Subject.objects.filter(class_section=student.student_class).order_by('name')

                # Build attendance matrix
                records = Attendance.objects.filter(student=student).order_by('date')
                dates = sorted(records.values_list('date', flat=True).distinct())
                sorted_dates = dates  # pass sorted dates to template

                # Initialize matrix with "-"
                for dt in dates:
                    for subj in subjects:
                        attendance_matrix[dt][subj.name.upper()] = "-"

                # Fill P/A
                for record in records:
                    status = "P" if record.status.lower() == "present" else "A"
                    attendance_matrix[record.date][record.subject.name.upper()] = status

                # Summary stats
                total_classes = records.count()
                present_count = records.filter(status__iexact="Present").count()
                attendance_percentage = round((present_count / total_classes) * 100, 1) if total_classes else 0

            except Student.DoesNotExist:
                messages.error(request, f"No student found with Roll Number {roll_number}.")
        else:
            messages.error(request, "Please enter your roll number.")

    return render(request, "student/attendance.html", {
        "student": student,
        "subjects": subjects,
        "attendance_matrix": attendance_matrix,
        "total_classes": total_classes,
        "present_count": present_count,
        "attendance_percentage": attendance_percentage,
        "sorted_dates": sorted_dates,
    })


# -------------------------------
# HOMEWORK VIEW
# -------------------------------
def homework_view(request):
    """
    Show homework for the student's class.
    """
    student = None
    homework_records = []

    if request.method == 'POST':
        roll_number = request.POST.get('roll_number', "").strip()
        if roll_number:
            try:
                student = Student.objects.get(roll_number=roll_number)
                homework_records = Homework.objects.filter(
                    class_section=student.student_class
                ).order_by('due_date')
                messages.success(request, f"✅ Homework loaded for Roll No: {roll_number}")
            except Student.DoesNotExist:
                messages.error(request, f"❌ No student found with Roll Number {roll_number}.")
        else:
            messages.error(request, "⚠️ Please enter your roll number.")

    return render(request, 'student/homework.html', {
        'student': student,
        'homework_records': homework_records
    })


# -------------------------------
# EXAMS VIEW
# -------------------------------
def exams_view(request):
    """
    Show exam schedule for the student's class.
    """
    student = None
    exam_records = []

    if request.method == 'POST':
        roll_number = request.POST.get('roll_number', "").strip()
        if roll_number:
            try:
                student = Student.objects.get(roll_number=roll_number)
                exam_records = Exam.objects.filter(
                    class_section=student.student_class
                ).order_by('exam_date')
                messages.success(request, f"✅ Exam schedule loaded for Roll No: {roll_number}")
            except Student.DoesNotExist:
                messages.error(request, f"❌ No student found with Roll Number {roll_number}.")
        else:
            messages.error(request, "⚠️ Please enter your roll number.")

    return render(request, 'student/exams.html', {
        'student': student,
        'exam_records': exam_records
    })


# -------------------------------
# PERFORMANCE VIEW
# -------------------------------
def performance_view(request):
    """
    Show student's performance per subject.
    """
    student = None
    performance_records = []

    if request.method == 'POST':
        roll_number = request.POST.get('roll_number', "").strip()
        if roll_number:
            try:
                student = Student.objects.get(roll_number=roll_number)
                performance_records = Performance.objects.filter(
                    student=student
                ).order_by('subject__name')
                messages.success(request, f"✅ Performance report loaded for Roll No: {roll_number}")
            except Student.DoesNotExist:
                messages.error(request, f"❌ No student found with Roll Number {roll_number}.")
        else:
            messages.error(request, "⚠️ Please enter your roll number.")

    return render(request, 'student/performance.html', {
        'student': student,
        'performance_records': performance_records
    })
