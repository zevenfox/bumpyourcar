from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from emergency.models import Location, Car


@api_view(['GET','PUT'])
# @permission_classes([IsAuthenticated])
def user_location(request, user_id):
    """
    API view for PUT request to post the location from geolocation API to the database or GET request to get the
    location of the user.

    :param request: HTTP request
    :param user_id: Target user ID
    :return: API response
    """
    try:
        location = Location.objects.get(user=user_id)
    except Location.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
def car_status(request, car_id):
    """
    API view for PUT request to update or GET request to get the status of the car.

    :param request: HTTP request
    :param car_id: Target car ID
    :return: API response
    """
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarStatusSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CarStatusSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_profile(request, user_id):
    """
    API view for GET request to get the profile of the user.

    :param request: HTTP request
    :param user_id: Target user ID
    :return: API response
    """
    try:
        profile = Profile.objects.get(id=user_id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_car(request, car_id):
    """
    API view for GET request to get the full car information from car ID.

    :param request: HTTP request
    :param user_id: Target user ID
    :return: API response
    """
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarFullSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)