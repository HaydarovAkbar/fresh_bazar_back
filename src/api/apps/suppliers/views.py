from .serializers import SuppliersSerializer
from rest_framework.filters import SearchFilter
from api.models.suppliers import Suppliers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser


class SuppliersView(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']

    def retrieve(self, request, *args, **kwargs):
        if kwargs['pk'] == '0':
            return Response({
                'name': None,
                'brand': None,
                'state': 1,
                'image': None,
                'weight': None,
                'price': None,
                'supply_date': None,
                'bar_code': None,
                'certificate': None,
                'market_share': None,
                'applied': False,
                'partnership': False,
                'unit_of_measure': 1,
            })
        pk_kwargs = kwargs['pk']
        category = Suppliers.objects.get(id=pk_kwargs)
        serializer = SuppliersSerializer(category)
        return Response(serializer.data)
