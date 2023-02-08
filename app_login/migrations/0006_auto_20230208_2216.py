# Generated by Django 3.2.10 on 2023-02-08 16:46

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0005_auto_20230208_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersignupmodel',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usersignupmodel',
            managers=[
                ('objects_original', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='usersignupmodel',
            name='username',
        ),
    ]