from rest_framework import viewsets

from .expert_models import Expert
from .expert_serializers import ExpertSerializer


class ExpertViewSet(viewsets.ModelViewSet):
    """"""

    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
