from django.contrib import admin

from connections.models import Connection


@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book",
        "user",
    )
    list_filter = ("book",)
    search_fields = (
        "book",
        "user",
    )
