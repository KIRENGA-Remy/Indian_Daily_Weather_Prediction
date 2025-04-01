from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ml_model.model import predict_weather
import pandas as pd

@api_view(['GET'])
def get_weather_prediction(request):
    forecast_days = int(request.query_params.get('days', 7))
    predictions = predict_weather(forecast_days=forecast_days)
    print(f"Predictions: {predictions}")
    dates = pd.date_range(start=pd.Timestamp.today(), periods=forecast_days).strftime('%Y-%m-%d').tolist()
    result = [{'date': date, 'meantemp': temp} for date, temp in zip(dates, predictions)]
    return Response(result)