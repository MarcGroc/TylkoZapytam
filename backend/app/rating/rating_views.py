from app.rating.rating_models import Rating
from app.rating.rating_serializers import RatingSerializer
from rest_framework import viewsets


class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.select_related()
    serializer_class = RatingSerializer
