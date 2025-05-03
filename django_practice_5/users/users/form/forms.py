from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def valid_username(self):
        name = self.cleaned_data.get('username')
        if len(name) < 4:
            raise forms.ValidationError("Username should be at least 4 characters long.")
        
        return name
    
    def password_match(self):
        password = self.cleaned_data.get("password")
        conf_password = self.cleaned_data.get("confirm_password")
        if password != conf_password:
            raise forms.ValidationError("Passwords don't match.")
        
        return password, conf_password