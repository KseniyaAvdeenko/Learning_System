from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegistrationForm, LoginUserForm
from .models import *


class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def home(request):
    users = CustomUser.objects.all()
    tasks = Tasks.objects.all()
    for_correct = MadeHw.objects.all()
    html = 'home.html'
    context = {'users': users, 'tasks': tasks, 'for_correct': for_correct}
    return render(request, html, context)

