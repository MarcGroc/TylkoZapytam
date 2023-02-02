from rest_framework import viewsets

from .call_models import Call
from .call_serializers import CallSerializer


class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.select_related()
    serializer_class = CallSerializer
