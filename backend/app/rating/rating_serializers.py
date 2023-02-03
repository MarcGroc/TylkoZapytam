from rest_framework import serializers

from app.rating.rating_models import Rating


class RatingSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Rating
        fields = "__all__"
        ordering = ["rating_date"]

        extra_kwargs = {"client": {"required": False}, "expert": {"required": False}}
