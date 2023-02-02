from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.client.client_models import Client
from users.expert.expert_models import Expert


class Rating(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=None
    )
    comment = models.TextField(max_length=300, default=None)
    rating_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)

    # TODO: add quetion id to prevent rating for the same question
    def __str__(self):
        return f"{self.client} to {self.expert} with {self.rating}"
