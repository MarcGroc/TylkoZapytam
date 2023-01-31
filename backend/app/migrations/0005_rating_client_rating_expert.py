# Generated by Django 4.1.5 on 2023-01-25 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_rename_user_client_client_id_and_more"),
        ("app", "0004_question_expert_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating",
            name="client",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.client",
            ),
        ),
        migrations.AddField(
            model_name="rating",
            name="expert",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.expert",
            ),
        ),
    ]