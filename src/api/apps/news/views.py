from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from api.models.news import News, Banner
from rest_framework.permissions import AllowAny

from .serializers import NewsSerializer, BannerSerializer
from api.pagination import DefaultPagination


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    pagination_class = DefaultPagination
    filter_backends = [SearchFilter]

    def get_queryset(self):
        queryset = News.objects.all()
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class BannerView(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [AllowAny]
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    # pagination_class = DefaultPagination
    filter_backends = [SearchFilter]
