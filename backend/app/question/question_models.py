from datetime import datetime

from django.db import models



class Question(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    question_text = models.TextField(max_length=1000, null=False)
    answer = models.TextField(max_length=1000, null=True, blank=True)
    question_date = models.DateTimeField(auto_now_add=True)
    answer_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        # Get the current date, hour, and minutes
        now = datetime.now()
        self.question_date = now.replace(second=0, microsecond=0)
        super().save(*args, **kwargs)
