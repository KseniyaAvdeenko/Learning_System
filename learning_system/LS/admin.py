from django.contrib import admin
from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'teacher',
        'is_staff',
        'date_joined',
        'user_profile'
    ]
    list_filter = ['is_staff', 'teacher']


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'made_hw',
        'correction_hw'
    ]
    list_filter = ['user']


class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['title']
    prepopulated_fields = {'slug': ('title',)}


class MadeHwAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'from_student']
    list_filter = ['task_id', 'from_student']


class CorrectionHwAdmin(admin.ModelAdmin):
    list_display = ['made_hw_id', 'feedback', 'mark']
    list_filter = ['id', 'made_hw_id']


admin.site.register(CorrectionHw, CorrectionHwAdmin),
admin.site.register(Tasks, TasksAdmin),
admin.site.register(Profile, ProfileAdmin),
admin.site.register(CustomUser, CustomUserAdmin),
admin.site.register(MadeHw, MadeHwAdmin)