from rest_framework import viewsets

from users.client.client_models import Client
from users.client.client_serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.select_related()
    serializer_class = ClientSerializer

