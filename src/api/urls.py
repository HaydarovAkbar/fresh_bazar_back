from django.urls import path, include
from rest_framework import routers

from api.apps.category import views as category
from api.apps.discount import views as discount
from api.apps.info import views as info
from api.apps.product import views as product
from api.apps.organizations import views as organization
from api.apps.orders import views as order
from api.apps.payments import views as payment
from api.apps.users import views as users


router = routers.DefaultRouter()


# Category
router.register(r'category', category.CategoryView, basename='category-api')
