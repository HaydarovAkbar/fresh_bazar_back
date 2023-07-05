from django.shortcuts import render
from .serializers import DiscountSerializer
from api.models.discount import Discount
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser


# Create your views here.

class DiscountView(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
