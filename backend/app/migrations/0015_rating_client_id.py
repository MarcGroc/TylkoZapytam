# Generated by Django 4.1.5 on 2023-01-24 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0012_remove_expert_ratings"),
        ("app", "0014_remove_question_expert_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="client_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.client",
            ),
        ),
    ]
