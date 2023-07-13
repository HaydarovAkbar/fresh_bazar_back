from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .serializers import UserSerializers, UserSerializersCreate
from api.filters import UserFilter
from api.pagination import DefaultPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from cryptography.fernet import Fernet


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
    serializer_class = UserSerializersCreate
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    parser_classes = (MultiPartParser,)

    def encrypt_data(self, data, encryption_key):
        cipher_suite = Fernet(encryption_key)
        encrypted_data = cipher_suite.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data, encryption_key):
        cipher_suite = Fernet(encryption_key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode()

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #     data['password'], key = encrypt(data['password'])
    #     data['key'] = key
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(is_superuser=False)
        serializer = UserSerializers(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializers(instance)
        return Response(serializer.data)
