# Generated by Django 4.1.5 on 2023-01-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_expert_working_hours"),
    ]

    operations = [
        migrations.AddField(
            model_name="expert",
            name="working_hours",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
