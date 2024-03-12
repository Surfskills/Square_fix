from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import IMUserSerializer
from .models import IMUser


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = IMUserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get("username")

        # Check if a user with the given username already exists
        if IMUser.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        # If username does not exist, proceed to create a new user
        new_user = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
