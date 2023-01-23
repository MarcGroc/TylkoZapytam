from django.urls import path

from .client.client_views import ClientAPIView, ClientDetailView
from .expert.expert_views import ExpertAPIView

urlpatterns = [
    path("client/<int:pk>", ClientAPIView.as_view(), name="client"),
    path("expert/<int:pk>", ExpertAPIView.as_view(), name="experts"),
    # below are for testing purposes
    path("detail/<int:pk>", ClientDetailView.as_view(), name="detail"),
]
