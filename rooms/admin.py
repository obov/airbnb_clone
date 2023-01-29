from django.contrib import admin
from .models import Room, Amenity


@admin.action(description="Set all prices to zero")
def rest_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (rest_prices,)
    list_display = (
        "name",
        "owner",
        "count_amenities",
        "rating",
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
    search_fields = (
        "name",
        "price",
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
