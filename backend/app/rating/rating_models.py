from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.expert.expert_models import Expert


class Rating(models.Model):
    app_label = "app"
    id = models.AutoField(primary_key=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    rating_date = models.DateTimeField(auto_now_add=True)
    # expert = models.ForeignKey(Expert, on_delete=models.CASCADE)