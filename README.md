# python_projects
---
# Voice-Controlled Assistant

## Introduction

The Voice-Controlled Assistant is a Python-based desktop assistant capable of understanding and executing basic voice commands. It interacts with users using speech and performs various actions such as telling jokes, opening websites, and giving time/date updates.

## Abstract

This project demonstrates the use of speech recognition and synthesis in building a simple voice assistant. The assistant uses the microphone input to listen to commands and responds accordingly. It includes basic natural language understanding and executes tasks like telling the time, date, jokes, and opening web pages. The goal is to enhance user productivity and accessibility via voice-based interfaces.

## Tools Used

Python

speech_recognition – to capture and recognize voice

pyttsx3 – for text-to-speech

webbrowser – to open websites

datetime – for date/time

pyjokes – for jokes

pyaudio – audio handling


## Steps Involved

1. Voice Input: Using speech_recognition, the assistant listens for user input.


2. Text Processing: The voice is converted into text and tokenized to understand intent.


3. Command Mapping: The assistant checks the tokens and triggers appropriate responses.


4. Voice Output: Using pyttsx3, the assistant speaks out the result.


5. Features Implemented:

Greet user

Tell jokes

Report time/date

Open websites

Detect “bye” to exit





---

# Real-Time Weather App

## Introduction

The Real-Time Weather App fetches and displays live weather data and forecasts for any city using the OpenWeatherMap API. Built using Streamlit, it is an interactive and visually informative tool.

## Abstract

This project showcases the integration of a public weather API with a Python-based web interface. Users can input any city name to retrieve and view current temperature, humidity, sunrise/sunset, and a 5-day forecast. The app uses dynamic charts and weather icons for better visual understanding.

## Tools Used

Python

Streamlit – UI and web app framework

requests – API communication

OpenWeatherMap API – weather data

matplotlib – for plotting forecasts

datetime – for time formatting


## Steps Involved

1. City Input: Users input city name through a Streamlit form.

2. API Call: Weather and forecast data fetched using requests.

3. Data Display:

Temperature, humidity, sunrise/sunset shown with icons.

Weather description is formatted and displayed.


4. Forecast Plotting: Using matplotlib, temperature trends are plotted over 5 days (3-hour intervals).

5. Unit Toggle: Users can select Celsius or Fahrenheit units.



## Conclusion

Both projects demonstrate practical implementation of Python for real-world applications:

The Voice Assistant improves hands-free productivity.

The Weather App delivers accurate environmental data in a visually pleasing format.

These projects enhance skills in APIs, automation, voice tech, and web interfaces—valuable in modern tech domains.


---
