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
from api.apps.news import views as news
from api.apps.suppliers import views as supplier

router = routers.DefaultRouter()
info_router = routers.DefaultRouter()
product_router = routers.DefaultRouter()
user_router = routers.DefaultRouter()
news_router = routers.DefaultRouter()
# Category api urls
router.register(r'category', category.ProductCategoryView, basename='category-api')

# info api urls
info_router.register(r'state', info.StateView, basename='state-api')
info_router.register(r'country', info.CountryView, basename='country-api')
info_router.register(r'district', info.DistrictView, basename='district-api')
info_router.register(r'region', info.RegionView, basename='region-api')
info_router.register(r'unit_of_measure', info.UnitOfMeasureView, basename='unit_of_measure-api')

# product api urls
product_router.register(r'product_inventory', product.ProductInventoryView, basename='product-inventory-api')
product_router.register(r'product', product.ProductView, basename='product-api')
product_router.register(r'discount', discount.DiscountView, basename='discount-api')
product_router.register(r'top_product', product.TopProductView, basename='top-product-api')
product_router.register(r'best_offer', product.BestOfferView, basename='best-offer-api')
product_router.register(r'product_rating', product.RatingProductView, basename='product-rating-api')
product_router.register(r'weekly_product', product.WeeklyProductView, basename='weekly-product-api')
product_router.register(r'filter_by_category', product.FilterByProductCategoryView, basename='filter-by-category-api')

# user api urls
user_router.register(r'users', users.UserView, basename='user-api')

# news api urls
news_router.register(r'news', news.NewsView, basename='news-api')
news_router.register(r'banner', news.BannerView, basename='banner-api')

# supplier api urls
router.register(r'supplier', supplier.SuppliersView, basename='supplier-api')

urlpatterns = router.urls + info_router.urls + product_router.urls + user_router.urls + news_router.urls
