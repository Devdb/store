from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User


class RegisterForm(UserForm):
    email = forms.EmailField(label='Email', max_length=100)


class LoginForm(UserForm):
    pass
