from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'requester_name', 'location', 'contact_number', 'type_of_service', 'initial_diagnosis', 'repair_option', 'service_time', 'booking_id']
