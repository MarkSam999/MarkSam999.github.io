from django import forms

class AnswerForm(forms.Form):
    user_answer = forms.IntegerField(label='Type here...', required=True)

