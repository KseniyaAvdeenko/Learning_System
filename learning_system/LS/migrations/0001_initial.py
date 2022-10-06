# Generated by Django 4.1.1 on 2022-10-04 13:18

import LS.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorrectionHw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_student', models.EmailField(default='', max_length=254)),
                ('feedback', models.TextField(blank=True)),
                ('mark', models.IntegerField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correction_hw', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='correct', to='LS.correctionhw')),
                ('marks', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LS.correctionhw', to_field='mark')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('teacher', models.BooleanField(default=False)),
                ('student', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='LS.profile')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', LS.managers.CustomUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='MadeHw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_student', models.EmailField(default='', max_length=254)),
                ('body', models.TextField(blank=True, null=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('is_corrected', models.BooleanField(default=False)),
                ('task_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='LS.tasks')),
            ],
        ),
        migrations.AddField(
            model_name='correctionhw',
            name='for_task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='LS.tasks'),
        ),
        migrations.AddField(
            model_name='correctionhw',
            name='from_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LS.profile'),
        ),
    ]