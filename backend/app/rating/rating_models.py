from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.client.client_models import Client


class Rating(models.Model):
    app_label = "app"
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    comment = models.TextField(max_length=300, null=True, blank=True)
    rating_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
