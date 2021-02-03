from django.contrib import admin

from modules.authorities.models import LocalGovernment


@admin.register(LocalGovernment)
class LocalGovernmentAdmin(admin.ModelAdmin):
    fields = ("id", ("created_at", "updated_at"), "region", "official_name")
    readonly_fields = ("id", "created_at", "updated_at")
    list_display = ("id", "official_name", "region")
    list_display_links = ("id", "official_name")


class LocalGovernmentInline(admin.TabularInline):
    model = LocalGovernment
    fields = ("id", "official_name", "created_at", "updated_at")
    readonly_fields = ("id", "created_at", "updated_at")
    extra = 0
