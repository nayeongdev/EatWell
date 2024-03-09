from django.contrib import admin
from restaurants.models import Restaurant, Comment, Tag


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",)
    }  # name 필드에 값이 입력됐을 때 자동으로 slug 생성


admin.site.register(Restaurant)
admin.site.register(Comment)
admin.site.register(Tag, TagAdmin)
