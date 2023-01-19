from rest_framework import serializers

from .question_models import Question


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # TODO: fields are only for testing purposes
        fields = ["id", "client", "expert", "question_date"]
