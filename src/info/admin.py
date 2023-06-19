from django.contrib import admin
from .models import State,Country,Region,District

# Register your models here.
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
