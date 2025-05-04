from django import forms
from .models import Student

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'edu_level', 'edu_mode', 'fav_course']
        widgets = {
            'name': forms.Select(attrs={'class': 'edu_level'})
        }