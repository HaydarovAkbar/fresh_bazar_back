from django.shortcuts import render

from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from api.models.product import Product
from ... import documents
from .serializers import ProductSerializer


class ProductViewSet(DocumentViewSet):
    document = documents.ProductDocument
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