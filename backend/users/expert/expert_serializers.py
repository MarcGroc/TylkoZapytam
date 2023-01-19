from rest_framework import serializers

from .expert_models import Expert


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        # TODO: fields are only for testing purposes
        fields = ["id", "ip_address", "questions_answered", "calls_scheduled"]
