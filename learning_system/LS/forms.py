from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms

from .models import CustomUser


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='First name', widget=forms.TextInput)
    last_name = forms.CharField(label='Last name', widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        label = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm password'
        }

class LoginUserForm(AuthenticationForm):
    class Meta:
        fields = ('email', 'password1')
        label = {
            'email': 'Email',
            'password1': 'Password',
        }
