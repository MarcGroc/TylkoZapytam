# Generated by Django 4.1.5 on 2023-02-01 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_alter_rating_client_alter_rating_comment_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rating",
            old_name="client",
            new_name="user",
        ),
    ]