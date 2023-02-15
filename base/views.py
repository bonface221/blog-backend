from rest_framework.response import Response
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import BlogSerializer, CategorySerializer
from .models import Blog, Category

# Create your views here.


class BlogViewSet(
    GenericViewSet, ListModelMixin, RetrieveModelMixin
):

    serializer_class = BlogSerializer

    def get_queryset(self):
        queryset = Blog.objects.all()
        category_id = self.request.query_params.get('category_id')

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class CategoryViewSet(GenericViewSet, ListModelMixin,):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
