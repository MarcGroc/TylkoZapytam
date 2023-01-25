# Generated by Django 4.1.5 on 2023-01-25 09:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Call",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("call_date", models.DateTimeField()),
                (
                    "call_duration",
                    models.IntegerField(
                        blank=True,
                        choices=[(10, 10), (15, 15), (20, 20), (25, 25), (30, 30)],
                        null=True,
                    ),
                ),
                (
                    "call_type",
                    models.CharField(
                        blank=True,
                        choices=[("Incoming", "Incoming"), ("outgoing", "Outgoing")],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "call_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("scheduled", "Scheduled"),
                            ("answered", "Answered"),
                            ("missed", "Missed"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question_text", models.TextField(max_length=1000)),
                ("answer", models.TextField(blank=True, max_length=1000, null=True)),
                ("question_date", models.DateTimeField(auto_now_add=True)),
                ("answer_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Rating",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "rating",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("comment", models.TextField(blank=True, max_length=300, null=True)),
                ("rating_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30, unique=True)),
            ],
        ),
    ]
