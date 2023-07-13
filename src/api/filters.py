import django_filters
from rest_framework.filters import BaseFilterBackend

from .models.users import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login']


class CategoryFilter(BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """

    def filter_queryset(self, request, queryset, view):
        param = request.QUERY_PARAMS.get('product_category', None)
        if param is not None:
            return queryset.filter(category=param)
        return queryset
