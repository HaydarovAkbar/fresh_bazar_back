from django.contrib import admin
from api.models.category import ProductInventory, Product

admin.site.site_header = 'help admin panel'
admin.site.register(Product)
admin.site.register(ProductInventory)