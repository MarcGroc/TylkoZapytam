# Generated by Django 4.1.5 on 2023-01-26 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_call_call_status_alter_call_call_type"),
        ("users", "0007_alter_expert_category_choices"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expert",
            name="category_choices",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.category",
            ),
        ),
    ]
