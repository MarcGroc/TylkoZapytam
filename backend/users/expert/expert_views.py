from django.contrib.auth.models import User
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework.views import APIView

from .expert_models import Expert
from .expert_serializers import ExpertSerializer
from ..serializers import UserSerializer


class ExpertAPIView(APIView):
    """This Endpoint returns expert by id"""

    def get(self, request, pk):
        expert = Expert.objects.get(user_id=pk)
        expert_serilizer = ExpertSerializer(expert)
        user = User.objects.get(id=pk)
        user_serilizer = UserSerializer(user)
        return Response({"client": expert_serilizer.data, "user": user_serilizer.data})

    def post(self, request, pk):
        expert = Expert.objects.get(user_id=pk)
        serializer = ExpertSerializer(expert)
        return Response(serializer.data)

    def put(self, request, pk):
        expert = Expert.objects.get(user_id=pk)
        serializer = ExpertSerializer(expert)
        return Response(serializer.data)

    def delete(self, request, pk):
        expert = Expert.objects.get(user_id=pk)
        serializer = ExpertSerializer(expert)
        return Response(serializer.data)


class ExpertDetailView(DetailView):
    model = Expert
    template_name = "expert_detail.html"
    context_object_name = "expert"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        expert = self.get_object()
        users = User.objects.filter(expert=expert)
        context["users"] = UserSerializer(users, many=True).data
        return context
