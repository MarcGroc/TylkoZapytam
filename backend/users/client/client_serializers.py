from rest_framework import serializers

from .client_models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "ip_address", "questions_asked", "calls_scheduled"]
