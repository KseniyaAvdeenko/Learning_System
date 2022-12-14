from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django import forms

from .models import *


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


class MakeHwForm(forms.ModelForm):
    class Meta:
        model = MadeHw
        fields = '__all__'
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': '"Write the answer of your homework"'
            }),
            'file': forms.FileInput(attrs={
                'class': "file",
                'multiple accept': "image/*"
            }),
        }


class CorrectHwForm(forms.ModelForm):
    class Meta:
        model = CorrectionHw
        fields = [
            'for_task',
            'for_student',
            'from_teacher',
            'feedback',
            'mark']
        label = {
            'mark': 'Mark',
        }
        widgets = {
            'feedback': forms.Textarea(attrs={
                'placeholder': '"Write the feedback"'
            }),
            'mark': forms.NumberInput()
        }


class MakeItCheckedForm(forms.ModelForm):
    class Meta:
        model = MadeHw
        fields = ['is_corrected']
        widgets = {
            'is_corrected': forms.CheckboxInput(attrs={
                'width': 18,
                'height': 18,

            })
        }


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'slug', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Write the title of the task",
                'class': 'input',
        }),
            'slug': forms.TextInput(attrs={
                'class': 'input-slug',
                'placeholder': "Write the slug of the task",
            }),

            'description': forms.Textarea(attrs={
                'placeholder': "Write the description of the task",
                'class': 'textarea',
            })
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'slug', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Write the title of the task",
                'class': 'input',
        }),
            'slug': forms.TextInput(attrs={
                'class': 'input-slug',
                'placeholder': "Write the slug of the task",
            }),

            'description': forms.Textarea(attrs={
                'placeholder': "Write the description of the task",
                'class': 'textarea',
            })
        }


class ChangeEmailForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email']

