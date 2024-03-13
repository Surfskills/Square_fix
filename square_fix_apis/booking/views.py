from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer

@api_view(['POST'])
def create_booking(request):
    # Retrieve the authenticated user
    user = request.user

    # Check if the user is a customer
    if user.user_type == 'CUSTOMER':
        # Proceed to create booking
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(requester_name=user)  # Assign the user as the requester
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Only customers can create bookings."}, status=status.HTTP_403_FORBIDDEN)