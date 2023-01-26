from app.call.call_views import CallViewSet
from app.category.category_views import CategoryViewSet
from app.question.question_views import QuestionViewSet
from app.rating.rating_views import RatingViewSet
from app.tag.tag_views import TagViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"call", CallViewSet, basename="call")
router.register(r"question", QuestionViewSet, basename="question")
router.register(r"rating", RatingViewSet, basename="rating")
router.register(r"tag", TagViewSet, basename="tag")

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
