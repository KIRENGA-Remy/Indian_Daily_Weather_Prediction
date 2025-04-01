import axios from 'axios';

const API_URL = 'http://localhost:8000/api/predict/';

export const fetchWeatherPrediction = async (days = 7) => {
    const response = await axios.get(`${API_URL}?days=${days}`);
    return response.data;
};