from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "player_name",
        "date",
        "start_time",
        "court_number",
        "surface",
    )
    list_filter = ("surface", "date")
    search_fields = ("player_name", "player_email")
