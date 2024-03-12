from rest_framework import serializers
from .models import IMUser

class IMUserSerializer(serializers.ModelSerializer):
    # Define a write-only password field
    password = serializers.CharField(write_only=True)

    class Meta:
        model = IMUser
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'phone_number', 'email', 'password']

    def create(self, validated_data):
        # Extract and remove the password from validated data
        password = validated_data.pop('password', None)
        
        # Create a new user instance
        user = IMUser.objects.create(**validated_data)

        # Set the password for the user
        if password:
            user.set_password(password)
            user.save()
        
        return user
