from rest_framework import viewsets

from .rating_models import Rating
from .rating_serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.select_related()
    serializer_class = RatingSerializer
