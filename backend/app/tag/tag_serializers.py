from rest_framework import serializers

from .tag_models import Tag


class TagSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Tag
        fields = ["name", "created"]
