from django.db import models
from users.client.client_models import Client
from users.expert.expert_models import Expert


class Call(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    call_date = models.DateTimeField()
    call_duration = models.IntegerField(
        choices=[(10, 10), (15, 15), (20, 20), (25, 25), (30, 30)],
        null=True,
        blank=True,
    )
    call_type = models.CharField(
        max_length=100,
        choices=[("Incoming", "Incoming"), ("outgoing", "Outgoing")],
        null=True,
        blank=True,
    )
    call_status = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=[
            ("scheduled", "Scheduled"),
            ("answered", "Answered"),
            ("missed", "Missed"),
        ],
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.client} to {self.expert} with {self.call_date}"
