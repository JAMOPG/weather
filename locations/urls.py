from django.urls import path
from locations.views import LocationView, forecast, weather


urlpatterns = [
    path('', LocationView.as_view()),
    path('forecast/', forecast, name='locations-forecast'),
    path('weather/', weather, name='locations-weather')
]