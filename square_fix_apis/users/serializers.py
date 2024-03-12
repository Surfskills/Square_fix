from rest_framework import serializers
from .models import IMUser

# UsersModelSerializer 
class IMUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IMUser
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'phone_number', 'email']
