from django.contrib import admin
from api.models.info import State, Country, Region, District, Language
from api.models.organizations import Organization
from api.models.product import ProductInventory, Product
from api.models.category import ProductCategory

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
