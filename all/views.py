from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Driver, DriverRequest, Reklama
from .serializers import DriverSerializer, DriverRequestSerializer, ReklamaSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


# Driver views
@api_view(['POST'])
def register_driver(request):
    serializer = DriverSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_driver_info(request, telegram_id):
    try:
        driver = Driver.objects.get(telegram_id=telegram_id)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)
    except Driver.DoesNotExist:
        return Response({'message': 'Driver not found'}, status=status.HTTP_404_NOT_FOUND)


class driver_list(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class driver_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


# Advertisement views
@api_view(['POST'])
def create_reklama(request):
    serializer = ReklamaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class reklama_list(generics.ListCreateAPIView):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer


class reklama_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reklama.objects.all()
    serializer_class = ReklamaSerializer


# Order views
@api_view(['POST'])
def request_driver(request):
    serializer = DriverRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def accept_driver(request):
    driver_id = request.data.get('driver_id')
    user_id = request.data.get('user_id')

    try:
        driver = Driver.objects.get(telegram_id=driver_id)
        driver_request = DriverRequest.objects.get(user_id=user_id)
        driver_request.is_accepted = True
        driver_request.driver = driver
        driver_request.save()
        return Response({'message': 'Driver request accepted'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'message': 'Error: ' + str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reject_driver(request):
    user_id = request.data.get('user_id')
    try:
        driver_request = DriverRequest.objects.get(user_id=user_id)
        driver_request.is_accepted = False
        driver_request.save()
        return Response({'message': 'Driver request rejected'}, status=status.HTTP_200_OK)
    except DriverRequest.DoesNotExist:
        return Response({'message': 'Driver request not found'}, status=status.HTTP_404_NOT_FOUND)


class driver_request_list(generics.ListCreateAPIView):
    queryset = DriverRequest.objects.all()
    serializer_class = DriverRequestSerializer


class driver_request_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriverRequest.objects.all()
    serializer_class = DriverRequestSerializer