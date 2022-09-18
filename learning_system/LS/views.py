from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView
from .forms import RegistrationForm, LoginUserForm, MakeHwForm, CorrectHwForm
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


def task_detail(request, task_slug):
    html = 'task_detail.html'
    task = get_object_or_404(Tasks, slug=task_slug)
    form = MakeHwForm()
    initial_obj = None
    if request.user.is_authenticated:
        initial_obj = {'from_student': request.user.get_full_name()}
    obj = Tasks.objects.get(slug=task_slug)

    if request.method == "POST":
        form = MakeHwForm(request.POST, request.FILES, initial=initial_obj, instance=obj)
        if form.is_valid():

            try:
                MadeHw.objects.create(**form.cleaned_data)
                answer = MadeHw(body=form.cleaned_data['body'], file=form.cleaned_data['file'])
                answer.save()
                return redirect("home")
            except IntegrityError as e:
                if 'unique constraint' in e.args:
                    pass

        else:
            form = MakeHwForm(initial=initial_obj, instance=obj)

    context = {
        'task': task,
        'form': form,
    }
    return render(request, html, context)


def correct_task(request, pk):
    html = 'tasks_for_correction.html'
    c_task = get_object_or_404(MadeHw, pk=pk)
    form = CorrectHwForm()
    # initial_obj = None
    # if request.user.is_authenticated:
    #     initial_obj = {'made': request.user.get_full_name()}
    obj = MadeHw.objects.get(pk=pk)
    #
    if request.method == "POST":
        form = CorrectHwForm(request.POST, instance=obj)
        if form.is_valid():
            try:
                CorrectionHw.objects.create(**form.cleaned_data)
                answer = CorrectionHw(feedback=form.cleaned_data['feedback'], mark=form.cleaned_data['mark'])
                answer.save()
                return redirect("home")
            except IntegrityError as e:
                if 'unique constraint' in e.args:
                    pass

        else:
            form = CorrectHwForm(instance=obj)

    context = {
        'c_task': c_task,
        'form': form,
    }
    return render(request, html, context)
