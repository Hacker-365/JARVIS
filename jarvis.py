# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!") 

    else:
        speak("Good Evening!")  
        print("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")  
    print("I am Jarvis Sir. Please tell me how may I help you")     

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")  
        speak("Recognition...")  
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        speak("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("Opening Youtube...")
            speak("Opening Youtube...")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("https://www.google.com/")

        elif 'open stackoverflow' in query:
            print("Opening StackOverFlow...")
            speak("Opening StackOverFlow...")
            webbrowser.open("https://stackoverflow.com/") 

        elif 'open hackerrank' in query:
            print("Opening Hackerrank...")
            speak("Opening Hackerrank...")
            webbrowser.open("https://www.hackerrank.com/dashboard")
        
        elif 'open dictionary' in query:
            print("Opening dictionary...")
            speak("Opening dictionary...")
            webbrowser.open("https://www.theopendictionary.com/")

        elif 'open game' in query:
            print("Opening Game...")
            speak("Opening Game...")
            webbrowser.open("https://codecombat.com/")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\91720\\Downloads\\VSCodeUserSetup-x64-1.94.2.exe"
            speak("Opening VScode...")
            print("Opening VScode...")
            os.startfile(codePath)

        elif 'open codepen' in query:
            print("Opening Codepen....")
            speak("Opening Codepen....")
            webbrowser.open("https://codepen.io/pen/")
            
        elif 'open chatgpt' in query:
            print("Opening ChatGPT...")
            speak("Opening ChatGPT...")
            webbrowser.open("https://chatgpt.com/")

        elif 'quit' or 'exit' in query:
            break
          
        else:
            print("No query matched")
