import speech_recognition as sr
from datetime import datetime
import pyttsx3
import os
from text_processing import commands

engine=pyttsx3.init()
engine.setProperty("rate",150)

def speak(text):
    try:
        engine.startLoop(False)
        if engine._inLoop:
            engine.endLoop()
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        engine.endLoop()
        engine.say(text)
        engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:   
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
        return command.lower()
    except sr.WaitTimeoutError as e:
        speak(e)
        return None
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        speak("Could not request results. Check your internet.")
        return None
def run_assistant():
    speak("Hello! I'm your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if not (commands(command)):
                break
            else:
                speak(commands(command))

run_assistant()
