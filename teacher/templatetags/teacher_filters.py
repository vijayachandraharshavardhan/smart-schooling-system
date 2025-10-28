from django import template
from student.models import Student
from teacher.models import ClassSection

register = template.Library()

@register.filter
def get_students(_, class_id):
    """
    Return all students of a given class ID ordered by roll_number
    """
    try:
        cls = ClassSection.objects.get(id=class_id)
        return Student.objects.filter(student_class=cls).order_by('roll_number')
    except ClassSection.DoesNotExist:
        return []
