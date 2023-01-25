from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "kind",
        "room",
        "experience",
    )
    list_filter = (
        "user",
        "kind",
        "room",
        "experience",
    )
