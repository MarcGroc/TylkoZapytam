from rest_framework import viewsets

from .client_models import Client
from .client_serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.select_related()
    serializer_class = ClientSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(user=self.request.user)
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
