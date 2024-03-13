from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Booking
from .serializers import BookingSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_booking(request):
    # Check if the authenticated user is a customer
    if not request.user.is_customer:
        return Response({"detail": "Only customers can create bookings."}, status=status.HTTP_403_FORBIDDEN)

    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        # Assign the requester (customer) to the booking
        serializer.save(requester=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
