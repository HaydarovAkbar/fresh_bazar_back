from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
)
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from api.models.product import Product, ProductInventory, TopProduct, BestOffer, RatingProduct
from api import documents
from .serializers import ProductSerializer, ProductInventorySerializer, TopProductSerializer, BestOfferSerializer, \
    RatingProductSerializer
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
            return Response({
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
            })
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
            return Response({
                # 'id': 0,
                'quantity': 1,
            })
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
            return Response({
                # 'id': 0,
                'product': 1,
            })
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
            return Response({
                'product': 1,
                'discount': None,
                'state': 1,
            })
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RatingProductView(viewsets.ModelViewSet):
    queryset = RatingProduct.objects.all()
    serializer_class = RatingProductSerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(
            data=data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'status': True,
                'message': 'Rating product successfully created',
                'data': serializer.data,
            }, status=201, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return Response({
                # 'id': 0,
                'product': 1,
                'rating': 5,
                'state': 1,
            })
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
