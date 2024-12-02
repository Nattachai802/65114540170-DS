from django import forms
from .models import *


class CourseForm(forms.ModelForm): 
    class Meta: 
          model = Course 
          fields = ['Course_id', 'Course_name', 'Teacher_name']