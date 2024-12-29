# Generated by Django 5.1.4 on 2024-12-29 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "patients",
            "0002_remove_patient_first_name_remove_patient_last_name_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="user",
        ),
        migrations.AddField(
            model_name="patient",
            name="first_name",
            field=models.CharField(default="john", max_length=100),
        ),
        migrations.AddField(
            model_name="patient",
            name="last_name",
            field=models.CharField(default="lname", max_length=100),
        ),
    ]
