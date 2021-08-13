from historics.models import Historic
from historics.serializers import HistoricSerializer
import requests
import json
from rest_framework import status as hstatus
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime


class HistoricView(APIView):
    
    def get(self, request):
        try:
            historics = Historic.objects.all()
        except Historic.DoesNotExist:
            return Response(
                {"message": "No locations registered."},
                 status=hstatus.HTTP_400_BAD_REQUEST)
        serialized = HistoricSerializer(historics, many=True)
        return Response(serialized.data, status=hstatus.HTTP_200_OK)
    
    
@api_view(['GET'])
def search_date(request):
    try:
        date = request.GET.get('date', None)
        date = datetime.strptime(date, '%d/%m/%Y')
        historics = Historic.objects.filter(created_at__date=date)
        serialized = HistoricSerializer(historics, many=True)                
    except APIException as e:
        print(e)
        return Response(e)
    return Response(serialized.data, status=hstatus.HTTP_200_OK)    