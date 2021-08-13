from django.shortcuts import render
import requests
import json
from rest_framework import status as hstatus
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from locations.models import Location
from locations.serializers import LocationSerializer
from weather.settings import OPENWEATHER_API_KEY, OPENWEATHER_API_URL


class LocationView(APIView):
    
    def get(self, request):
        try:
            locations = Location.objects.filter(country='BR')
        except Location.DoesNotExist:
            return Response(
                {"message": "No locations registered."},
                 status=hstatus.HTTP_400_BAD_REQUEST)
        serialized = LocationSerializer(locations, many=True)
        return Response(serialized.data, status=hstatus.HTTP_200_OK)
    
    
@api_view(['GET'])
def forecast(request):
    try:
        location = request.GET.get('q', None)
        units = request.GET.get('units', None)
        params = {'q': location,
                  'units': units,
                  'appid': OPENWEATHER_API_KEY}
        url = OPENWEATHER_API_URL+'/forecast'
        response = requests.get(url=url, params=params)
        status = hstatus.HTTP_200_OK if response.status_code == 200 else hstatus.HTTP_404_NOT_FOUND
        response = json.loads(response.content)
    except APIException as e:
        print(e)
        return Response(e)    
    return Response(response, status=status)


@api_view(['GET'])
def weather(request):
    try:
        location = request.GET.get('q', None)
        units = request.GET.get('units', None)
        params = {'q': location,
                  'units': units,
                  'appid': OPENWEATHER_API_KEY}
        url = OPENWEATHER_API_URL+'/weather'
        response = requests.get(url=url, params=params)
        status = hstatus.HTTP_200_OK if response.status_code == 200 else hstatus.HTTP_404_NOT_FOUND
        response = json.loads(response.content)
    except APIException as e:
        print(e)
        return Response(e)    
    return Response(response, status=status)
