from django.contrib import admin
from restaurants.models import Restaurant, Comment, Tag

admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Tag)
