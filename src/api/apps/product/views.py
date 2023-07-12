from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
)
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from api.models.product import Product, ProductInventory, TopProduct, BestOffer
from api import documents
from .serializers import ProductSerializer, ProductInventorySerializer, TopProductSerializer, BestOfferSerializer
from api.pagination import DefaultPagination
from rest_framework.response import Response


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

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return {
                # 'id': 0,
                'name': None,
                'description': None,
                'price': 0,
                'sku': None,
                'image': None,
                'category': 1,
                'inventory': None,
                'discount': None,
                'state': 1,
            }
        instance = self.get_object()
        instance.views += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ProductInventoryView(viewsets.ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return {
                # 'id': 0,
                'quantity': 1,
            }
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TopProductView(viewsets.ModelViewSet):
    queryset = TopProduct.objects.all()
    serializer_class = TopProductSerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return {
                # 'id': 0,
                'product': 1,
            }
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BestOfferView(viewsets.ModelViewSet):
    queryset = BestOffer.objects.all()
    serializer_class = BestOfferSerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return {
                # 'id': 0,
                'name': None,
                'description': None,
                'image': None,
                'state': 1,
            }
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
