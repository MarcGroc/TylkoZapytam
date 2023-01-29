from app.tag.tag_models import Tag
from django.db import models


class Category(models.Model):
    app_label = "app"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, unique=True, blank=False)
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
