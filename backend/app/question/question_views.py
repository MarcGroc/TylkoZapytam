from rest_framework import viewsets

from .question_models import Question
from .question_serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.select_related()
    serializer_class = QuestionSerializer
