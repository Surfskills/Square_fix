from django.contrib.auth.models import AbstractUser
from django.db import models

class IMUser(AbstractUser):
    USER_TYPES = (
        ('SHOP', 'REPAIRER'),
        ('CUSTOMER', 'SMARTPHONE OWNER'),
        ('ADMIN', 'SYSTEM ADMINISTRATOR'),
    )
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=155, blank=True)
    last_name = models.CharField(max_length=155, blank=True)
    middle_name = models.CharField(max_length=155, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='CUSTOMER')
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def delete(self, *args, **kwargs):
        # Soft delete by setting is_active to False
        self.is_active = False
        self.save(update_fields=['is_active'])
