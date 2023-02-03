from rest_framework import viewsets

from users.expert.expert_models import Expert
from users.expert.expert_serializers import ExpertSerializer


class ExpertViewSet(viewsets.ModelViewSet):

    queryset = Expert.objects.select_related()
    serializer_class = ExpertSerializer

