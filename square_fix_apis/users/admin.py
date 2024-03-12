from django.contrib import admin
from .models import IMUser

class IMUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'user_type', 'date_created']

admin.site.register(IMUser, IMUserAdmin)
