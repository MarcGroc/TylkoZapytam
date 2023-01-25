# Generated by Django 4.1.5 on 2023-01-23 11:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_tag_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.RemoveField(
            model_name="category",
            name="tags",
        ),
        migrations.AddField(
            model_name="category",
            name="tags",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.tag",
            ),
        ),
    ]
