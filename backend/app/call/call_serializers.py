from rest_framework import serializers

from .call_models import Call


class CallSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Call
        fields = "__all__"
