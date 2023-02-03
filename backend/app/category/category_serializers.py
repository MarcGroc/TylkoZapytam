from rest_framework import serializers

from app.category.category_models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "tags"]
