from django.contrib import admin

from .models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    fields = ("id", ("created_at", "updated_at"), "name", "population")
    readonly_fields = ("id", "created_at", "updated_at")
    list_display = ("id", "name", "population")
    list_display_links = ("id", "name")
