from django.contrib import admin

# Register your models here.
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'date')
    list_display_links = ('id', 'customer_name')
    search_fields = ('date', 'customer_name')
    list_filter = ('date', 'time')