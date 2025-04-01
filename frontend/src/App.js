import React, { useState } from 'react';
import WeatherForm from './components/WeatherForm';
import WeatherDisplay from './components/WeatherDisplay';
import './App.css';

function App() {
    const [predictions, setPredictions] = useState([]);

    return (
        <div className="App">
            <h1>Weather Prediction for India</h1>
            <WeatherForm setPredictions={setPredictions} />
            <WeatherDisplay predictions={predictions} />
        </div>
    );
}

export default App;