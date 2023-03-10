from rest_framework import serializers
from users.expert.expert_models import Expert


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = [
            "id",
            "ip_address",
            "questions_answered",
            "calls_scheduled",
            "expert_is_verified",
        ]
