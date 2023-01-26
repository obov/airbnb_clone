from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "count_amenities",
        "price",
        "kind",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "description",
        "address",
        "is_pet_allowed",
        "kind",
        "owner",
        "amenitis",
        "category",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
