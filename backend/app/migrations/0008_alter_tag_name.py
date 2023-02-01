# Generated by Django 4.1.5 on 2023-02-01 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_call_call_status_alter_call_call_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(
                max_length=30,
                unique=True,
                validators=[
                    django.core.validators.MinValueValidator(3),
                    django.core.validators.MaxValueValidator(30),
                ],
            ),
        ),
    ]