from rest_framework import serializers

from .call_models import Call


class CallSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Call
        fields = ["call_date", "call_duration", "call_type", "call_status", "created"]
