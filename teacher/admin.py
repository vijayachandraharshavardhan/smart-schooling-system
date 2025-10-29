from django.contrib import admin
from .models import Teacher, ClassSection, Attendance, Homework, Exam, Performance, Subject
from student.models import Student  # just imported, do NOT register here

# -----------------------------
# Teacher Admin
# -----------------------------
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'class_section', 'joined_date')
    list_filter = ('class_section', 'subject')
    search_fields = ('name', 'email')


# -----------------------------
# ClassSection Admin
# -----------------------------
@admin.register(ClassSection)
class ClassSectionAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section')
    search_fields = ('class_name', 'section')


# -----------------------------
# Subject Admin
# -----------------------------
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_section')
    list_filter = ('class_section',)
    search_fields = ('name',)


# -----------------------------
# Attendance Admin
# -----------------------------
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_section', 'subject', 'date', 'status', 'teacher')
    list_filter = ('class_section', 'subject', 'date', 'status')
    search_fields = ('student__name', 'class_section__class_name')


# -----------------------------
# Homework Admin
# -----------------------------
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('subject', 'class_section', 'due_date')
    list_filter = ('class_section', 'subject', 'due_date')
    search_fields = ('subject__name', 'class_section__class_name')


# -----------------------------
# Exam Admin
# -----------------------------
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', 'class_section', 'exam_date', 'max_marks')
    list_filter = ('class_section', 'subject', 'exam_date')
    search_fields = ('subject__name', 'class_section__class_name')


# -----------------------------
# Performance Admin
# -----------------------------
@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_section', 'subject', 'marks', 'updated_at')
    list_filter = ('class_section', 'subject', 'updated_at')
    search_fields = ('student__name', 'class_section__class_name')



