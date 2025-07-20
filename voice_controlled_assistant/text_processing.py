import re
import webbrowser
import random
from datetime import datetime

def text_processing(user_input):
    clean_text = user_input.lower()
    clean_text = re.sub(r'[^\w\s]', '', clean_text)
    tokens = clean_text.split()
    return tokens
def commands(user_input):
    while True:
        now=datetime.now()
        tokens=text_processing(user_input)
        if "hello" in tokens or "hi" in tokens:
            greetings = ["Hello boss! How can I help you?", "Hey there!", "Hi! What can I do for you today?"]
            response = random.choice(greetings)
        elif "name" in tokens:
            response = "I’m a basic chatbot."
        elif "how are you" in user_input:
            response = "I'm doing great, thanks! How about you?" 
        elif "i am fine" in user_input or "i'm fine" in user_input:
            responses = ["Glad to hear that! 😊", "Awesome!", "Great! Let me know if you need anything."]
            response = random.choice(responses)
        elif user_input in ["what about you"] :
            responses = [
                "I'm doing great, thanks for asking! 😊",
                "All good on my side! Ready when you are 😄",
                "Just another day helping awesome people like you!",
                "Feeling fantastic! Let's get to it 🚀"
                ]
            response = random.choice(responses)
        elif user_input in ["introduce","who are you","introduce you"]:
            response = "Hi there! I'm Chatbot, your friendly AI chatbot. I'm here to help with Python, tech, or anything you're curious about!"
        elif "sad" in tokens:
            response = "I'm here for you. Want to hear a joke to cheer up?"

        elif "happy" in tokens:
            response = "Yay! I'm happy too!"

        elif "joke" in tokens:
            jokes = [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the computer go to the doctor? Because it had a virus!",
                "Why was the math book sad? Because it had too many problems."
                ]
            response = random.choice(jokes)
        elif "time" in tokens:
            response=f"The time is {now.strftime("%H:%M")}"
        elif "date" in tokens:
            response=f"The date is {now.strftime("%d-%m-%Y")}"
        elif "website" in tokens:
            web_link=input("link:")
            url=f"https://{web_link}"
            webbrowser.open(url)
            response="Did you have complete the work?"
        elif user_input in ["yes","also done",'s'] :
            response = " Ok,fine.What do next?"
        elif ["thank you","thankyou"] in tokens:
            response="You are welcome sir!" 
        elif user_input.lower() == "bye" or "goodbye" in tokens:
            response="Bye! Have a nice day."
            break
        else:
            unknown = [
                "Sorry, I didn’t understand that.",
                "Hmm... I'm not sure what you mean.",
                "Can you please say that differently?"
                ]
            response = random.choice(unknown)
        return response
    return response
