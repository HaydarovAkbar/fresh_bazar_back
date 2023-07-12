from django.shortcuts import render
from .serializers import StateSerializer, CountrySerializer, DistrictSerializer, RegionSerializer, \
    UnitOfMeasureSerializer
from api.models.info import State, Country, District, Region, UnitOfMeasure
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response


# Create your views here.

class StateView(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return Response({
                'shortname': None,
                'fullname': None,
                'code': None,
                'postal_code': None,
                'state': 1,
            })
        pk_kwargs = kwargs['pk']
        country = Country.objects.get(id=pk_kwargs)
        serializer = CountrySerializer(country)
        return Response(serializer.data)


class DistrictView(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return Response({
                'shortname': None,
                'fullname': None,
                'code': None,
                'region': 1,
                'state': 1,
            })
        pk_kwargs = kwargs['pk']
        district = District.objects.get(id=pk_kwargs)
        serializer = DistrictSerializer(district)
        return Response(serializer.data)


class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return Response({
                'shortname': None,
                'fullname': None,
                'code': None,
                'country': 1,
                'state': 1,
            })
        pk_kwargs = kwargs['pk']
        region = Region.objects.get(id=pk_kwargs)
        serializer = RegionSerializer(region)
        return Response(serializer.data)


class UnitOfMeasureView(viewsets.ModelViewSet):
    queryset = UnitOfMeasure.objects.all()
    serializer_class = UnitOfMeasureSerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return Response({
                'name': None,
                'abbreviation': None,
                'state': 1,
            })
        pk_kwargs = kwargs['pk']
        state = State.objects.get(id=pk_kwargs)
        serializer = StateSerializer(state)
        return Response(serializer.data)
