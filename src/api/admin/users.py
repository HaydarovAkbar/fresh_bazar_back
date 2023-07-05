from django.contrib import admin
from api.models.users import User

admin.site.site_header = 'help admin panel'
admin.site.register(User)