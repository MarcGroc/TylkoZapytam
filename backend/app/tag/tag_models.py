from django.db import models


class Tag(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30, null=False)

    def __str__(self):
        return self.name
