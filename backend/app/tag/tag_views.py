from rest_framework import viewsets

from .tag_models import Tag
from .tag_serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.select_related()
    serializer_class = TagSerializer
