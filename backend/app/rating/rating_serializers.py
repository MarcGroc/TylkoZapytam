from rest_framework import serializers

from .rating_models import Rating


class RatingSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Rating
        fields = "__all__"
        ordering = ["rating_date"]
