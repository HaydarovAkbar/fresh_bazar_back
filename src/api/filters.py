import django_filters

from .models.users import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_login']