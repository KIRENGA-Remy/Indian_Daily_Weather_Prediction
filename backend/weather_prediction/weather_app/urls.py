from django.urls import path
from .views import get_weather_prediction

print("Weather app URLs loaded")  # Confirm this file is loaded

urlpatterns = [
    path('predict/', get_weather_prediction, name='predict_weather'),
]

print("Weather app URL patterns:", urlpatterns)  # Show the registered patterns