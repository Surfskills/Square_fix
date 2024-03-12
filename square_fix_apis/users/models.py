from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class IMUser(AbstractUser):
    USER_TYPES = (
        ('SHOP', 'REPAIRER'),
        ('CUSTOMER', 'SMARTPHONE OWNER'),
        ('ADMIN', 'SYSTEM ADMINISTRATOR'),
    )
    first_name = models.CharField(max_length=155, blank=True)
    last_name = models.CharField(max_length=155, blank=True)
    middle_name = models.CharField(max_length=155, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='CUSTOMER')
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
