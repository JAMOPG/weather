from locations.views import LocationView
from django.urls import path
from frontend import views


urlpatterns = [
    path('', views.index ),
    
]