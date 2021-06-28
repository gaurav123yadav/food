from django import forms
from .models import User

# User Form 
class RegisterForm(forms.ModelForm):

    class Meta:
        model = User

        fields= [
            'email',
            'password'
        ]

class LoginForm(forms.ModelForm):

    class Meta:
        model = User

        fields= [
            'email',
            'password'
        ]