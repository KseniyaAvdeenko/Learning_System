from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='first name', max_length=30)
    last_name = models.CharField(verbose_name='last name', max_length=30)
    email = models.EmailField(unique=True)
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_profile = models.OneToOneField('Profile', null=True, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    marks = models.ManyToManyField('CorrectionHw', related_name='marks')
    correction_hw = models.ManyToManyField('CorrectionHw')

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task', kwargs={'task_slug': self.slug})


class MadeHw(models.Model):
    task_id = models.ForeignKey(
        Tasks,
        on_delete=models.CASCADE,
        null=True,
        default=''
    )
    from_student = models.EmailField(default='')
    body = models.TextField(blank=True, null=True)
    file = models.ImageField(upload_to='media/', blank=True, null=True)
    is_corrected = models.BooleanField(default=False)


class CorrectionHw(models.Model):
    for_task = models.ForeignKey(
        Tasks,
        on_delete=models.CASCADE,
        default=''
    )
    for_student = models.EmailField(default='')
    from_teacher = models.ForeignKey(Profile, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True)
    mark = models.IntegerField(unique=True, blank=True)

    def __str__(self):
        return str(self.mark)

