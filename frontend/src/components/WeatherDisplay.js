import React from 'react';

const WeatherDisplay = ({ predictions }) => {
    if (!predictions.length) return <p>No predictions yet.</p>;

    return (
        <div>
            <h2>Weather Predictions</h2>
            <ul>
                {predictions.map((pred, index) => (
                    <li key={index}>
                        {pred.date}: {pred.meantemp.toFixed(2)}°C
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default WeatherDisplay;