from rest_framework import viewsets

from .category_models import Category
from .category_serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related()
    serializer_class = CategorySerializer
