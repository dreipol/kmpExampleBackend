from django.contrib import admin

from api.models import Content


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass
