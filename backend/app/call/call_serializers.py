from app.call.call_models import Call
from rest_framework import serializers


class CallSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Call
        fields = "__all__"
