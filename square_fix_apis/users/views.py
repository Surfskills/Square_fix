from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .serializers import IMUserSerializer
from .models import IMUser
from django.contrib.auth import authenticate



#Registration
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

    #User signing in
from .serializers import IMUserSerializer

from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import IMUserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    # Receive inputs and validate
    username = request.data.get("username")
    password = request.data.get("password")

    if not username or not password:
        return Response({"detail": "Please provide both username and password"}, status=status.HTTP_400_BAD_REQUEST)

    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)  # Log in the user
        serializer = IMUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
