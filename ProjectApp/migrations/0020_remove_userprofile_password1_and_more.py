# Generated by Django 4.1 on 2022-08-31 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ProjectApp", "0019_userprofile_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="password1",),
        migrations.RemoveField(model_name="userprofile", name="password2",),
    ]
