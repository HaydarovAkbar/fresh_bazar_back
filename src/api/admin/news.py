from .info import admin
from api.models.news import News

admin.site.site_header = 'help admin panel'
admin.site.register(News)