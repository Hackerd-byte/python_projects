# 🎙️ Voice_Controlled Assistant 

A simple voice-controlled assistant built using Python. It listens to your voice commands, processes them, and responds back with text-to-speech. It can greet you, tell jokes, give you the time and date, and open websites, among other things.


---

## 📂 Project Structure

### 📦 voice_assistant
├── main.py               # Entry point: listens and responds to user commands
├── text_processing.py    # Handles text parsing and response logic
└── README.md             # Documentation


---

## ⚙️ Requirements

Install the required packages:
```
pip install SpeechRecognition pyttsx3 pyaudio
```
> Note: If you face issues installing pyaudio, use:

Windows: Download the .whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

Linux: sudo apt-get install portaudio19-dev before installing





---

## 🚀 How to Run
```
python main.py
```
Once you run it, your assistant will start listening to your voice and respond accordingly.


---

## 🧠 Features

🤖 Greets and responds conversationally

😂 Tells jokes

⏰ Tells the current time and date

🌐 Opens a website on voice command

🧽 Basic text pre-processing and command matching

🎤 Supports Google Speech Recognition



---

## 🎯 Example Commands

Command	Action
```
"Hello" / "Hi"	Greets you
"Tell me a joke"	Tells a random joke
"What is the time?"	Speaks the current time
"What is today's date?"	Speaks today's date
"Open website"	Prompts and opens a web URL
"Bye"	Ends the assistant
```


---

## 📌 Notes

Requires an internet connection (for Google Speech API).

Make sure your microphone is enabled.

Runs in a loop until you say "Bye".



---


