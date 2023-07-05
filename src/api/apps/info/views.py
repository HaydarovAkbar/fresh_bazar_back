from django.shortcuts import render
from .serializers import StateSerializer, CountrySerializer, DistrictSerializer, RegionSerializer
from api.models.info import State, Country, District, Region
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser


# Create your views here.

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']
