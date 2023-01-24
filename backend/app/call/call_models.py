from django.db import models


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
        max_length=50,
        choices=[("Incoming", "Incoming"), ("outgoing", "Outgoing")],
        null=True,
        blank=True,
    )
    call_status = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        choices=[
            ("scheduled", "Scheduled"),
            ("answered", "Answered"),
            ("missed", "Missed"),
        ],
    )

    def __str__(self):
        return f"{self.id} on {self.call_date}"
