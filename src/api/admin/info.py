from django.contrib import admin
from api.models.info import State, Country, Region, District, Language
from api.models.organizations import Organization

admin.site.site_header = 'Министерство спорта Республики Узбекистан'
admin.site.register(State)
admin.site.register(Language)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(District)
admin.site.register(Organization)


