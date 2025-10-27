from django import forms
from .models import Subject, Attendance

class AttendanceForm(forms.Form):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
