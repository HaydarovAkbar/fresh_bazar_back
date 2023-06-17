from django.shortcuts import render

from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from .models import Product
from .documents import ProductDocument
from .serializers import ProductSerializer


class ProductViewSet(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductSerializer
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
    ]
    search_fields = (
        'name',
        'description',
    )
    filter_fields = {
        'name': 'name.raw',
    }
    queryset = Product.objects.all()

