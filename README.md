This project is a Django-based REST API that leverages machine learning (specifically LSTM neural networks) to predict daily weather conditions in the Delhi region. The predictions are based on historical meteorological data, including mean temperature, humidity, wind speed, and pressure. This tool aims to support researchers, environmentalists, and policymakers by providing accurate and up-to-date climate information.

Table of Contents

Features
Technologies Used
Getting Started
Prerequisites
Installation
API Usage
Model Training
Contributing
License
Acknowledgments

Features
Predicts mean temperature for the next 7 days using historical data.
Built with an LSTM neural network for time-series forecasting.
Exposes predictions via a REST API using Django REST Framework.
Provides easy integration for researchers and policymakers.
Supports scalability for additional meteorological variables (e.g., humidity, wind speed).

Technologies Used
Backend Framework : Django
Machine Learning Library : TensorFlow/Keras
Data Processing : Pandas, NumPy, Scikit-learn
API Framework : Django REST Framework
Database : SQLite (default), but can be extended to PostgreSQL or MySQL
Deployment : Can be deployed on platforms like AWS, Heroku, or Azure.

Getting Started
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8 or higher (Download Python )
Pip (Python package manager)
Virtualenv (optional but recommended for isolating dependencies)

Installation
Clone the Repository
git clone https://github.com/KIRENGA-Remy/Indian_Daily_Weather_Prediction.git
cd Indian_Daily_Weather_Prediction

Set Up a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate

Install Dependencies

pip install -r requirements.txt
Prepare the Dataset
Ensure the dataset (weather_data.csv) is placed in the appropriate directory (backend/weather_prediction/weather_app/ml_model/).
The dataset should include columns such as date, meantemp, humidity, wind_speed, and pressure.
Run Migrations

python manage.py migrate
Start the Development Server

python manage.py runserver
The API will now be accessible at:

http://127.0.0.1:8000/api/
API Usage
Endpoint: /api/get_weather_prediction/
Request Method: GET
Query Parameters:
days (optional): Number of days for which predictions are required. Default is 7.
Example Request:

curl "http://127.0.0.1:8000/api/get_weather_prediction/?days=7"
Example Response:


[
    {"date": "2023-10-20", "meantemp": 25.3},
    {"date": "2023-10-21", "meantemp": 26.1},
    {"date": "2023-10-22", "meantemp": 24.9},
    {"date": "2023-10-23", "meantemp": 23.7},
    {"date": "2023-10-24", "meantemp": 22.5},
    {"date": "2023-10-25", "meantemp": 21.8},
    {"date": "2023-10-26", "meantemp": 20.4}
]
Model Training
To train the LSTM model:

Navigate to the ml_model directory:

cd backend/weather_prediction/weather_app/ml_model
Run the training script:

python model.py
The trained model will be saved as trained_model.h5 in the specified directory.
Contributing
We welcome contributions to improve this project! Here’s how you can help:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeatureName).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeatureName).
Open a pull request.
Please ensure your code adheres to the project’s coding standards and includes appropriate documentation.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thanks to the contributors of open-source libraries like TensorFlow, Django, and Pandas.
Special thanks to the Indian Meteorological Department for providing publicly available meteorological data.
Inspired by the need for accurate climate research tools to address environmental challenges.