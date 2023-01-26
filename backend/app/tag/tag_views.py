from rest_framework import viewsets

from .tag_models import Tag
from .tag_serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
