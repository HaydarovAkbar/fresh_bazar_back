from django.shortcuts import render

from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
)
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from api.models.product import Product, ProductInventory, TopProduct
from api import documents
from .serializers import ProductSerializer, ProductInventorySerializer, TopProductSerializer
from api.pagination import DefaultPagination

class ProductView(viewsets.ModelViewSet):
    # document = documents.ProductDocument
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    # lookup_field = 'id'
    # filter_backends = [
    #     FilteringFilterBackend,
    #     SearchFilterBackend,
    # ]
    search_fields = (
        'name',
        'description',
        'price',
    )
    # filter_fields = {
    #     'name': 'name.raw',
    # }
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']


class ProductInventoryView(viewsets.ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']


class TopProductView(viewsets.ModelViewSet):
    queryset = TopProduct.objects.all()
    serializer_class = TopProductSerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']