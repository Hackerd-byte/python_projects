import streamlit as st
import requests
from datetime import datetime
import matplotlib.pyplot as plt

API_KEY = '0673a03098dc1a3c4fa2c761c56abcc2' 
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

def get_weather(city, units='metric'):
    weather_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units={units}"
    forecast_url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units={units}"

    weather_data = requests.get(weather_url).json()
    forecast_data = requests.get(forecast_url).json()
    return weather_data, forecast_data
st.title("Real-Time Weather App")
city = st.text_input("Enter City Name", "Chennai")
unit = st.radio("Select Unit", ["Celsius", "Fahrenheit"])
unit_key = 'metric' if unit == 'Celsius' else 'imperial'

if st.button("Get Weather"):
    weather, forecast = get_weather(city, unit_key)

    if weather.get("cod") != 200:
        st.error(f"City '{city}' not found!")
    else:
        st.subheader(f"Weather in {city}")
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        sunrise = datetime.utcfromtimestamp(weather['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.utcfromtimestamp(weather['sys']['sunset']).strftime('%H:%M:%S')
        icon = weather['weather'][0]['icon']
        description = weather['weather'][0]['description'].capitalize()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", f"{temp} °{unit[0]}")
            st.metric("Humidity", f"{humidity}%")
        with col2:
            st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png", width=80)
            st.write(description)

        st.write(f"*Sunrise*: {sunrise} UTC")
        st.write(f"*Sunset*: {sunset} UTC")
        st.subheader("5-Day Forecast (Every 3 hrs)")
        times = []
        temps = []

        for item in forecast['list']:
            times.append(item['dt_txt'])
            temps.append(item['main']['temp'])

        plt.figure(figsize=(10, 4))
        plt.plot(times, temps, marker='o')
        plt.xticks(rotation=45)
        plt.xlabel("Date Time")
        plt.ylabel(f"Temp (°{unit[0]})")
        plt.title(f"Forecast for {city}")
        plt.tight_layout()
        st.pyplot(plt)
