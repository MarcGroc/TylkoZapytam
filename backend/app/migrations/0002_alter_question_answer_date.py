# Generated by Django 4.1.5 on 2023-01-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="answer_date",
            field=models.DateTimeField(null=True),
        ),
    ]