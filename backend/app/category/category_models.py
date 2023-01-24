from django.db import models


class Category(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, unique=True, blank=False)

    def __str__(self):
        return self.name
