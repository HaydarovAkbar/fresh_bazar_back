from django.contrib.auth.models import User
from .serializers import UserSerializers
from api.filters import UserFilter
from api.pagination import DefaultPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from cryptography.fernet import Fernet
from rest_framework.response import Response


def encrypt(message):
    key = Fernet.generate_key()  # Key generation for encryption
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(message.encode())  # Encryption
    return encrypted_data, key


def decrypt(key, message):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(message)  # Decryption
    return decrypted_data


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
