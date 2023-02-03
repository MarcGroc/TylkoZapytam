from rest_framework import serializers

from app.question.question_models import Question


class QuestionSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Question
        fields = "__all__"
