from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # TODO: fields are only for testing purposes

        fields = [
            "username",
            "first_name",
            "is_active",
            "is_superuser",
            "last_login",
            "date_joined",
        ]
