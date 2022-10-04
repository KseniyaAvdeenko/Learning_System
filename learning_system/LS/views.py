from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.db.models import Avg, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .forms import RegistrationForm, LoginUserForm, MakeHwForm, CorrectHwForm, AddTaskForm, UpdateTaskForm
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
    for_correct = MadeHw.objects.filter(is_corrected=False).all()
    html = 'home.html'
    context = {
        'users': users,
        'tasks': tasks,
        'for_correct': for_correct,

    }
    return render(request, html, context)


def task_detail(request, task_slug):
    html = 'task_detail.html'
    task = get_object_or_404(Tasks, slug=task_slug)
    feedback = CorrectionHw.objects.filter(Q(for_student=request.user.email) & Q(for_task=task.pk))
    form = MakeHwForm()
    initial_obj = None
    if request.user.is_authenticated:
        initial_obj = {'from_student': request.user.email, 'is_corrected': False}
    if request.method == "POST":
        form = MakeHwForm(request.POST, request.FILES, initial=initial_obj)
        if form.is_valid():

            try:
                answer = MadeHw(
                    task_id=form.cleaned_data['task_id'],
                    from_student=form.cleaned_data['from_student'],
                    body=form.cleaned_data['body'],
                    file=form.cleaned_data['file'],
                )
                answer.save()
                return redirect("home")
            except IntegrityError as e:
                if 'unique constraint' in e.args:
                    pass

    else:
        form = MakeHwForm(initial=initial_obj)

    context = {
        'task': task,
        'form': form,
        'feedback': feedback
    }
    return render(request, html, context)


def correct_task(request, pk):
    html = 'tasks_for_correction.html'
    c_task = get_object_or_404(MadeHw, pk=pk)
    obj = {
        'for_student': c_task.from_student,
        "from_teacher": request.user.email
    }
    form = CorrectHwForm(initial=obj)
    if request.method == "POST":
        form = CorrectHwForm(request.POST, initial=obj)
        if form.is_valid():
            try:
                answer = CorrectionHw(
                    for_task=form.cleaned_data['for_task'],
                    for_student=form.cleaned_data['for_student'],
                    from_teacher=form.cleaned_data['from_teacher'],
                    feedback=form.cleaned_data['feedback'],
                    mark=form.cleaned_data['mark']
                )
                answer.save()
                return redirect("home")
            except IntegrityError as e:
                if 'unique constraint' in e.args:
                    pass

        else:
            form = CorrectHwForm(initial=obj)

    context = {
        'c_task': c_task,
        'form': form,
    }
    return render(request, html, context)


def show_feedback(request, pk):
    html = 'feedback.html'
    task = get_object_or_404(Tasks, pk=pk)
    feedback = CorrectionHw.objects.filter(for_student=request.user.email).get(for_task=task.pk)
    stud_answer = MadeHw.objects.filter(from_student=request.user.email).get(task_id=task.pk)
    context = {
        'task': task,
        'feedback': feedback,
        'stud_answer': stud_answer
    }
    return render(request, html, context)


def profile(request, pk):
    html = 'profile.html'
    user = CustomUser.objects.get(pk=pk)
    users = CustomUser.objects.all()
    stud_quantity = CustomUser.objects.filter(student=True).all()
    teach_quantity = CustomUser.objects.filter(teacher=True).all()
    tasks_for_c = MadeHw.objects.filter(is_corrected=False).all()
    task_q = Tasks.objects.all()
    c_task_q = CorrectionHw.objects.filter(for_student=request.user.email).all()

    def avg_mark():
        for a in CorrectionHw.objects.filter(for_student=request.user).values('mark').all().aggregate(res=Avg('mark')).values():
            return a

    context = {
        'user': user,
        'users': users,
        'stud_quantity': stud_quantity,
        'tasks_for_c': tasks_for_c,
        'task_q': task_q,
        'avg_mark': avg_mark,
        'teach_quantity': teach_quantity,
        'c_task_q': c_task_q
    }
    return render(request, html, context)


class AddTask(CreateView):
    form_class = AddTaskForm
    template_name = 'add_task.html'
    success_url = reverse_lazy('home')


class UpdateTask(UpdateView):
    model = Tasks
    form_class = UpdateTaskForm
    template_name = 'task_edit.html'
    slug_url_kwarg = 'task_slug'
    success_url = reverse_lazy('home')


class DeleteTask(DeleteView):
    model = Tasks
    template_name = 'task_delete.html'
    slug_url_kwarg = 'task_slug'
    success_url = reverse_lazy('home')


def show_members(request, pk):
    html = 'members.html'
    user = CustomUser.objects.get(pk=pk)
    users = CustomUser.objects.all()
    students = CustomUser.objects.filter(student=True).all()
    teachers = CustomUser.objects.filter(teacher=True).all()
    context = {
        'students': students,
        'user': user,
        'users': users,
        'teachers': teachers
    }
    return render(request, html, context)


