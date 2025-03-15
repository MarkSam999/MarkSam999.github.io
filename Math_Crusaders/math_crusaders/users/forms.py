from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile
from main_app.models import News_Post
from chats.models import Message

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This nickname is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email is taken')
        return email

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254, widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise ValidationError("No such email")

            if not user.check_password(password):
                raise ValidationError("Incorrect password")
            
            if not user.is_active:
                raise ValidationError("This account is inactive")

            cleaned_data['user'] = user
        return cleaned_data

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username'
            ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'image'
            ]

class NewsPostForm(forms.ModelForm):
    class Meta:
        model = News_Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={
                'style': 'resize: none; width: 100%; place-self: center;',
            }),
        }    

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'style': 'resize: none; width: 100%; font-size: 20px; text-align: left; place-self: center; height: 100%;',
            }),
        }
    def save(self, user=None, commit=True):
        chat_message = super().save(commit=False)
        if user:
            chat_message.posted_by = user
        if commit:
            chat_message.save()
        return chat_message  