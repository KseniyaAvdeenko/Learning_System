from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('correction/<int:pk>/', views.correct_task, name='correct_task'),
    path('task/<slug:task_slug>/', views.task_detail, name='task_detail'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('add_task/', AddTask.as_view(), name='add_task'),
    path('task/<slug:task_slug>/edit', UpdateTask.as_view(), name='edit_task'),
    path('task/<slug:task_slug>/delete/', DeleteTask.as_view(), name='delete_task'),
    path('profile/<int:pk>/members/', views.show_members, name='members'),
    path('feedback/<int:pk>/', views.show_feedback, name='feedback'),
    path('make_it_checked/<int:pk>/', views.make_it_checked, name="make_it_checked"),
    path('profile/<int:pk>/change_email', ChangeEmail.as_view(), name='change_email'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]

