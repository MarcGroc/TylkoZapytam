from django.db import models

# from backend.users.client.client_models import Client


class Rating(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    rating = models.IntegerField(range(1, 6), null=True, blank=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    rating_date = models.DateTimeField(auto_now_add=True)
    # client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    # expert_id = models.ForeignKey(Expert, on_delete=models.CASCADE, null=True, blank=True)
