from django.urls import path
from api import views

urlpatterns = [
    path('api/ev-metrics', views.ev_metrics),
    path('api/ev-5min', views.ev_5min),
    path('api/journeys', views.journeys),
    path('api/journey-route', views.journey_route),
]