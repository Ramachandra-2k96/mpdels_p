from django import forms
from .models import StudentRegistration
class inputform(forms.ModelForm):
    class Meta:
        model=StudentRegistration
        fields=['name','college_name','course_name']
