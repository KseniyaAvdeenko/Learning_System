# Generated by Django 4.1.1 on 2022-10-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LS', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='correction_hw',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='marks',
        ),
        migrations.AddField(
            model_name='profile',
            name='correction_hw',
            field=models.ManyToManyField(to='LS.correctionhw'),
        ),
        migrations.AddField(
            model_name='profile',
            name='marks',
            field=models.ManyToManyField(related_name='marks', to='LS.correctionhw'),
        ),
    ]
