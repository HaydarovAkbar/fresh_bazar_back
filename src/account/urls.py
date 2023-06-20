from django.urls import path
from .views import CustomModalViewSet

urlpatterns = [
    path('', CustomModalViewSet.as_view({'get': 'list', 'post': 'create'}), name='custom_modal_viewset'),
]
