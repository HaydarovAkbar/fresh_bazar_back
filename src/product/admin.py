from django.contrib import admin
from .models import Product, ProductInventory, ProductCategory

admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductCategory)
