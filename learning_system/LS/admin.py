from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'teacher',
        'student',
        'is_staff',
        'date_joined',
        'user_profile'
    ]
    list_filter = ['is_staff', 'teacher', 'student']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']


class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}


class MadeHwAdmin(admin.ModelAdmin):
    list_display = [
        'task_id',
        'from_student',
        'file',
        'is_corrected'
    ]
    list_filter = [
        'task_id',
        'from_student',
        'is_corrected'
        ]


class CorrectionHwAdmin(admin.ModelAdmin):
    list_display = [
        'for_task',
        "for_student",
        'from_teacher',
        'feedback',
        'mark']
    list_filter = [
        'id',
        'for_task',
        'from_teacher',
        'for_student']


admin.site.register(CorrectionHw, CorrectionHwAdmin),
admin.site.register(Tasks, TasksAdmin),
admin.site.register(Profile, ProfileAdmin),
admin.site.register(CustomUser, CustomUserAdmin),
admin.site.register(MadeHw, MadeHwAdmin)