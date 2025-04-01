import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.layers.core import Dense
from tensorflow.python.keras import models
from tensorflow.python.keras import layers
from sklearn.preprocessing import MinMaxScaler
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), 'weather_data.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../trained_model.h5')

def prepare_data(days=30, forecast_days=7):
    # Load and preprocess data
    df = pd.read_csv(DATA_PATH)
    df['date'] = pd.to_datetime(df['date'])
    data = df[['meantemp']].values
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    # Create sequences
    X, y = [], []
    for i in range(days, len(scaled_data) - forecast_days + 1):
        X.append(scaled_data[i-days:i])
        y.append(scaled_data[i:i+forecast_days])
    X, y = np.array(X), np.array(y)
    return X, y, scaler

def train_model():
    X, y, scaler = prepare_data()
    model = models.Sequential()
    model.add(layers.LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(layers.LSTM(50))
    model.add(layers.Dense(7))  # Predicting 7 days
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=20, batch_size=32)
    model.save(MODEL_PATH)
    return model, scaler

def predict_weather(days=30, forecast_days=7):
    print(f"Predicting weather for {forecast_days} days with {days} days of history")
    if not os.path.exists(MODEL_PATH):
        print("Model not found, training new model")
        model, scaler = train_model()
    else:
        print("Loading existing model")
        model = models.load_model(MODEL_PATH)
        _, _, scaler = prepare_data()

    df = pd.read_csv(DATA_PATH)
    print(f"Last {days} days of data shape: {df[['meantemp']].values[-days:].shape}")
    last_sequence = scaler.transform(df[['meantemp']].values[-days:])
    last_sequence = last_sequence.reshape((1, days, 1))
    prediction = model.predict(last_sequence)
    prediction = scaler.inverse_transform(prediction)
    print(f"Raw prediction: {prediction}")
    return prediction.flatten().tolist()

if __name__ == "__main__":
    # Train model initially (run once)
    train_model()