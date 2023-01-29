from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.client.client_models import Client
from users.expert.expert_models import Expert


class Rating(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    comment = models.TextField(max_length=300, null=True, blank=True)
    rating_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, null=True, blank=True)
