# Generated by Django 4.1 on 2022-08-31 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ProjectApp", "0024_photo_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="profile_pic",
            field=models.ImageField(upload_to=""),
        ),
    ]
