from app.question.question_models import Question
from app.question.question_serializers import QuestionSerializer
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.select_related()
    serializer_class = QuestionSerializer
