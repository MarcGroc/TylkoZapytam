
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Expert",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, max_length=300, null=True),
                ),
                ("available", models.BooleanField(default=False)),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True, null=True, unpack_ipv4=True
                    ),
                ),
                ("ip_city", models.CharField(blank=True, max_length=100, null=True)),
                ("country_code", models.CharField(blank=True, max_length=2, null=True)),
                ("device_type", models.CharField(blank=True, max_length=50, null=True)),
                ("last_password_change", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        default="expertimg.jpg",
                        null=True,
                        upload_to="experts_avatars",
                    ),
                ),
                ("question_price", models.IntegerField(default=0)),
                ("questions_answered", models.IntegerField(default=0)),
                ("call_price", models.IntegerField(default=0)),
                ("calls_scheduled", models.IntegerField(default=0)),
                ("calls_completed", models.IntegerField(default=0)),
                (
                    "category_choices",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=100),
                        default=list,
                        size=None,
                    ),
                ),
                ("expert_is_verified", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["questions_answered", "calls_scheduled"],
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True, null=True, unpack_ipv4=True
                    ),
                ),
                ("ip_city", models.CharField(blank=True, max_length=100, null=True)),
                ("country_code", models.CharField(blank=True, max_length=2, null=True)),
                ("device_type", models.CharField(blank=True, max_length=50, null=True)),
                ("last_password_change", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("questions_asked", models.IntegerField(default=0)),
                ("calls_scheduled", models.IntegerField(default=0)),
                ("calls_completed", models.IntegerField(default=0)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["questions_asked", "calls_scheduled"],
            },
        ),
    ]
