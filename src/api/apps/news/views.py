from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from api.models.news import News
from .serializers import NewsSerializer
from api.pagination import DefaultPagination


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
