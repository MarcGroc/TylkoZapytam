from rest_framework import serializers

from .call_models import Call


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        # TODO: fields are only for testing purposes
        fields = ["id", "call_date", "call_duration", "call_type", "call_status"]
