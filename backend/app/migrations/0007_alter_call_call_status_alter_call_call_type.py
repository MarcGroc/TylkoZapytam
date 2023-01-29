# Generated by Django 4.1.5 on 2023-01-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_call_client_call_expert"),
    ]

    operations = [
        migrations.AlterField(
            model_name="call",
            name="call_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("scheduled", "Scheduled"),
                    ("answered", "Answered"),
                    ("missed", "Missed"),
                ],
                max_length=100,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="call",
            name="call_type",
            field=models.CharField(
                blank=True,
                choices=[("Incoming", "Incoming"), ("outgoing", "Outgoing")],
                max_length=100,
                null=True,
            ),
        ),
    ]
