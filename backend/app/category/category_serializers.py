from rest_framework import serializers

from .category_models import Category


# class TagSerializer(serializers.ModelSerializer):
#     created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
#
#     class Meta:
#         model = Tag
#         fields = ["name", "created"]


class CategorySerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True)
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Category
        fields = ["name", "tags", "created"]
