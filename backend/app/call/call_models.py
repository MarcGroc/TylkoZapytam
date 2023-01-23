from datetime import datetime

from django.db import models


class Call(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    call_date = models.DateTimeField(auto_now_add=True)
    call_duration = models.IntegerField(null=True, blank=True)
    call_type = models.CharField(max_length=100, null=True, blank=True)
    call_status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.call_date

    def save(self, *args, **kwargs):
        # Get the current date, hour, and minutes
        now = datetime.now()
        self.call_date = now.replace(second=0, microsecond=0)
        super().save(*args, **kwargs)
