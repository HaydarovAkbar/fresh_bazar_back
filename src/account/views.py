from django.contrib.auth.models import User
from .serializers import UserSerializers
from .filters import UserFilter
from .pagination import CustomPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter


class CustomModalViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]

    def get_queryset(self):
        queryset = self.queryset
        if hasattr(self.queryset.model, 'username'):
            queryset = self.queryset.exclude(username__exact='')

        return queryset
