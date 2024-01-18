from functions.online import jokes, wikipedia_search
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os import calculator, camera, cmd, notepad, discord
from random import choice
from loading import loading


USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 190)

engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = datetime.now().hour
    print("Current hour:", hour)  
    if 6 <= hour < 12:
        speak(f"Good Morning {USERNAME}")
    elif 12 <= hour < 16:
        speak(f"Good afternoon {USERNAME}")
    elif 16 <= hour < 19:
        speak(f"Good Evening {USERNAME}")
    else:
        speak(f"good night {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


def input():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(loading))
        else:
            hour = datetime.now().hour
            if hour <= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet()
    while True:
        query = input().lower()

        if 'open notepad' in query:
            notepad()

        elif 'open discord' in query:
            discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            cmd()

        elif 'open camera' in query:
            camera()

        elif 'open calculator' in query:
            calculator()

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = input().lower()
            results = wikipedia_search(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = jokes()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

        elif 'exit' in query or 'stop' or 'thank you' in query:
            hour = datetime.now().hour
            if hour <= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()