from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import HelloView

urlpatterns = [
    path("test", HelloView.as_view(), name="test"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
