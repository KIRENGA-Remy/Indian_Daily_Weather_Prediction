from rest_framework import serializers
from .models import WeatherPrediction

class WeatherPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherPrediction
        fields = ['date', 'meantemp']