from rest_framework import serializers

from .category_models import Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "tags"]
