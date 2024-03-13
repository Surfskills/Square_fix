from django.db import models
from users.models import IMUser

class Booking(models.Model):
    REPAIR_OPTIONS = (
        ('STORE', 'At the Store'),
        ('RIDER', 'Rider Delivery'),
        ('HOME', 'Home Service'),
    )
    
    requester_name = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    type_of_service = models.CharField(max_length=100)
    initial_diagnosis = models.TextField()
    repair_option = models.CharField(max_length=20, choices=REPAIR_OPTIONS)
    service_time = models.DateTimeField()
    booking_id = models.CharField(max_length=100)

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Requester_name: {self.requester_name}"
