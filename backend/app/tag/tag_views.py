from app.tag.tag_models import Tag
from app.tag.tag_serializers import TagSerializer
from rest_framework import viewsets


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.select_related()
    serializer_class = TagSerializer
