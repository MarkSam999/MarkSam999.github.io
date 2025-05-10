from django import forms

class MathQuestionForm(forms.Form):
    answer = forms.IntegerField(
        label="Выбери правильный ответ",
        widget=forms.RadioSelect
    )

    def __init__(self, *args, choices=None, **kwargs):
        super().__init__(*args, **kwargs)
        if choices:
            self.fields['answer'].choices = choices