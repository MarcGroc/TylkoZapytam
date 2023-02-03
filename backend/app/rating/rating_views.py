from rest_framework import viewsets

from app.rating.rating_models import Rating
from app.rating.rating_serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.select_related()
    serializer_class = RatingSerializer
