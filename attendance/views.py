def attendance_view(request):
    student = None
    subjects = []
    attendance_matrix = defaultdict(dict)
    total_classes = present_count = 0
    attendance_percentage = 0
    sorted_dates = []  # <-- this is new

    if request.method == "POST":
        roll_number = request.POST.get("roll_number", "").strip()
        if roll_number:
            try:
                student = Student.objects.get(roll_number=roll_number)
                subjects = Subject.objects.filter(class_section=student.student_class).order_by('name')

                records = Attendance.objects.filter(student=student).order_by('date')
                for record in records:
                    date = record.date
                    subject_name = record.subject.name.upper()
                    attendance_matrix[date][subject_name] = (
                        "P" if record.status.lower() == "present" else "A"
                    )

                total_classes = records.count()
                present_count = records.filter(status__iexact="Present").count()
                attendance_percentage = round((present_count / total_classes) * 100, 1) if total_classes > 0 else 0

                sorted_dates = sorted(attendance_matrix.keys())  # <-- important

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
