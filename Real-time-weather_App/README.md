# Real-Time Weather App

This is a simple, interactive web app built with Streamlit that displays real-time weather and 5-day forecasts for any city using the OpenWeatherMap API.

## Features

Get current weather data: temperature, humidity, sunrise, sunset.

Display dynamic weather icons and description.

5-day weather forecast chart (every 3 hours).

Toggle between Celsius and Fahrenheit.

Responsive layout with visualizations using matplotlib.


## Tech Stack

Python

Streamlit

Requests (API calls)

Matplotlib (for forecast chart)

OpenWeatherMap API


## How to Run

1. Install dependencies:
```
pip install streamlit requests matplotlib
```

2. Run the app:
```
streamlit run weatherapi.py
```


## API Key

Replace the placeholder API key in the script:

API_KEY = 'your_openweathermap_api_key'

You can get your free API key by signing up at: https://openweathermap.org/api

##  Example Usage

Input a city name like Erode.

Choose unit: Celsius or Fahrenheit.

Click Get Weather to fetch current and forecast data.


##  File Structure
```
weatherapi.py        
README.md           
```


## Screenshots

Here's how the app looks in actions
![Weather app Screenshot1](images/Screenshot(1).png)
![Weather app Screenshot2](images/Screenshot(2).png)




