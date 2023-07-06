from .info import admin
from api.models.category import ProductInventory, Product

admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.site_header = 'help admin pane'