from app.category.category_models import Category
from app.category.category_serializers import CategorySerializer
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related()
    serializer_class = CategorySerializer
