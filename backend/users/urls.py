from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.client.client_views import ClientViewSet
from users.expert.expert_views import ExpertViewSet

router = DefaultRouter()
router.register("client", ClientViewSet, basename="client")
router.register("expert", ExpertViewSet, basename="expert")

urlpatterns = [
    path("api/", include(router.urls)),
]
