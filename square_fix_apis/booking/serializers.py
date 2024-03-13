from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'requester_name', 'location', 'contact_number', 'type_of_service', 'initial_diagnosis', 'repair_option', 'service_time', 'booking_id']
