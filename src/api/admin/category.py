from django.contrib import admin
from api.models.category import ProductCategory

admin.site.site_header = 'help admin panel'
admin.site.register(ProductCategory)