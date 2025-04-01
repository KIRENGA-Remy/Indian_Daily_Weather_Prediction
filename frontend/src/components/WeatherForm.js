import React, { useState } from 'react';
import { fetchWeatherPrediction } from '../api/weatherApi';

const WeatherForm = ({ setPredictions }) => {
    const [days, setDays] = useState(7);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await fetchWeatherPrediction(days);
        setPredictions(data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Days to Predict:
                <input
                    type="number"
                    value={days}
                    onChange={(e) => setDays(e.target.value)}
                    min="1"
                    max="30"
                />
            </label>
            <button type="submit">Predict Weather</button>
        </form>
    );
};

export default WeatherForm;