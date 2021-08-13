from django.urls import path
from historics.views import search_date, HistoricView


urlpatterns = [
    path('', HistoricView.as_view()),
    path('search_date/', search_date, name='historics-search-date'),
]