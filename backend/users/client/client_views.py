from django.contrib.auth.models import User
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserSerializer
from .client_models import Client
from .client_serializers import ClientSerializer


class ClientAPIView(APIView):
    """This Endpoint returns  a client by id"""

    def get(self, request, pk):
        client = Client.objects.get(user_id=pk)
        client_serilizer = ClientSerializer(client)
        user = User.objects.get(id=pk)
        user_serilizer = UserSerializer(user)
        return Response({"client": client_serilizer.data, "user": user_serilizer.data})

    def post(self, request, pk):
        client = Client.objects.get(user_id=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        client = Client.objects.get(user_id=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def delete(self, request, pk):
        client = Client.objects.get(user_id=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)


class ClientDetailView(DetailView):
    model = Client
    template_name = "client_detail.html"
    context_object_name = "client"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.get_object()
        users = User.objects.filter(client=client)
        context["users"] = UserSerializer(users, many=True).data
        return context
