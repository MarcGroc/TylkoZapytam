from app.call.call_models import Call
from app.call.call_serializers import CallSerializer
from rest_framework import viewsets


class CallViewSet(viewsets.ModelViewSet):
    queryset = Call.objects.select_related()
    serializer_class = CallSerializer
