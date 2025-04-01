from django.db import models

# Create your models here.

class WeatherPrediction(models.Model):
    date = models.DateField()
    meantemp = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)