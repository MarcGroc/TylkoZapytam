from app.tag.tag_models import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Tag
        fields = ["name", "created"]
