from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
    path('task/<slug:task_slug>/delete/', DeleteTask.as_view(), name='delete_task')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)