from django.urls import path
from .views import get_weather_prediction

urlpatterns = [
    path('predict/', get_weather_prediction, name='predict_weather'),
]
