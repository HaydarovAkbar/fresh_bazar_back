from django.contrib import admin
from api.models.info import State, Country, Region, District, Language
from api.models.organizations import Organization
from api.models.product import ProductInventory, Product, TopProduct
from api.models.category import ProductCategory
from api.models.discount import Discount
from api.models.news import News

admin.site.site_header = 'help admin panel'
admin.site.register(State)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Organization)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(TopProduct)
admin.site.register(Discount)
admin.site.register(News)