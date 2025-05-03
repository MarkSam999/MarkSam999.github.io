from .models import Student
from django import forms

class ChoiceForm(forms.ModelForm):
    class Meta:
        Model = Student
        fields = ['name', 'edu_level', 'edu_modes', 'fav_course']