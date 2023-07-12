from django.shortcuts import render
from .serializers import DiscountSerializer
from api.models.discount import Discount
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response


# Create your views here.

class DiscountView(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return Response({
                'name': None,
                'description': None,
                'value': None,
                'discount_percent': None,
                'image': None,
                'state': 1,
            })
        pk_kwargs = kwargs['pk']
        discount = Discount.objects.get(id=pk_kwargs)
        serializer = DiscountSerializer(discount)
        return Response(serializer.data)
