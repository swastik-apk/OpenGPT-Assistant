# Importing dependencies.

import openai
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import os

engine = pyttsx3.init()
listener = sr.Recognizer()
load_dotenv()
key = os.environ.get("SECRET_KEY")
openai.api_key = key

while True:
    with sr.Microphone() as source:
        print("Dictate your Query: ")
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        model = "text-davinci-003"

    base = openai.Completion.create(model = "text-davinci-003",
    prompt = data,
    max_tokens = 1024,
    temperature = 0.5,
    n = 1,
    stop = None)

    response = base.choices[0].text # type: ignore

    choice = int(input("Press 0 to print the response OR 1 to print & hear the response: "))

    if choice == 0:
        print(response)
    else:
        print(response)
        engine.say(response)
        engine.runAndWait()
    
    repeat = input("Do you want to continue or exit ? ")
    if repeat == "exit":
        break