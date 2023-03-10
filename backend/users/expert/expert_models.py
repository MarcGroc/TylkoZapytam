# from app.category.category_models import Category
from django.contrib.auth.models import User
from django.db import models


class Expert(models.Model):
    app_label = "users"

    expert = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, max_length=300)
    available = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(
        protocol="both", unpack_ipv4=True, blank=True, null=True
    )
    ip_city = models.CharField(max_length=100, null=True, blank=True)
    country_code = models.CharField(max_length=2, null=True, blank=True)
    device_type = models.CharField(max_length=200, null=True, blank=True)
    last_password_change = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    avatar = models.ImageField(
        upload_to="experts_avatars", null=True, blank=True, default="expertimg.jpg"
    )
    question_price = models.IntegerField(default=0)
    questions_answered = models.IntegerField(default=0)
    call_price = models.IntegerField(default=0)
    calls_scheduled = models.IntegerField(default=0)
    calls_completed = models.IntegerField(default=0)
    # category_choices = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, null=True, blank=True
    # )
    expert_is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ["questions_answered", "calls_scheduled"]

    def __str__(self):
        return self.expert.username
