# from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    app_label = "users"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(
        protocol="both", unpack_ipv4=True, blank=True, null=True
    )
    ip_city = models.CharField(max_length=100, null=True, blank=True)
    country_code = models.CharField(max_length=2, null=True, blank=True)
    device_type = models.CharField(max_length=50, null=True, blank=True)
    last_password_change = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    questions_asked = models.IntegerField(default=0)
    calls_scheduled = models.IntegerField(default=0)
    calls_completed = models.IntegerField(default=0)

    class Meta:
        ordering = ["questions_asked", "calls_scheduled"]

    def __str__(self):
        return self.user.username
