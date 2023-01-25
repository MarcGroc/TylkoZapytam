from rest_framework import serializers

from .question_models import Question


class ClientSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Question
        fields = ["id", "question_text" "created_at"]
