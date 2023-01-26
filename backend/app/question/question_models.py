from django.db import models
from users.client.client_models import Client
from users.expert.expert_models import Expert


class Question(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    question_text = models.TextField(max_length=1000, null=False)
    answer = models.TextField(max_length=1000, null=True, blank=True)
    question_date = models.DateTimeField(auto_now_add=True)
    answer_date = models.DateTimeField(null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    expert_id = models.ForeignKey(
        Expert, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.question_text
