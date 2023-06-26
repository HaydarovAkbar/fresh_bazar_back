from django.contrib import admin
from api.models.info import State, Country, Region, District
from api.models.organizations import Organization

admin.site.site_header = 'Admin Panel'
admin.site.register(State)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)


admin.site.register(Organization)