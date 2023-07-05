from django.shortcuts import render
from .serializers import ProductCategorySerializer
from rest_framework.filters import SearchFilter
from api.models.category import ProductCategory
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser


# class ProductCategoryView(APIView):
#     def get(self, request):
#         category = ProductCategory.objects.all()
#         serializer = ProductCategorySerializer(category, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ProductCategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductCategoryView(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filter_backends = [SearchFilter]
    # permission_classes = AllowAny
    parser_classes = (MultiPartParser,)
    http_method_names = ['get', 'post', 'put', 'delete']
    search_fields = ['name', 'description']
