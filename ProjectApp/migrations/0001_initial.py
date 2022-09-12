# Generated by Django 4.1 on 2022-08-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=60)),
                ("last_name", models.CharField(max_length=60)),
                ("email", models.EmailField(max_length=254)),
                ("born_date", models.DateField()),
                ("age", models.IntegerField()),
                ("phone_number", models.IntegerField()),
                ("city", models.CharField(max_length=50)),
                ("Country", models.CharField(max_length=100)),
            ],
        ),
    ]