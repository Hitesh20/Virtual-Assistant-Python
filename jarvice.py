import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)

def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(os.environ.get('USER'), os.environ.get('PASS'))
        server.sendmail("hiteshmunjal22@gmail.com", to, content)
        server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Hitesh")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Hitesh")
    else:
        speak("Good Evening Hitesh")
    speak("I am Jarvice. How may I help you?")

def takeCommand():
    # Takes microphone input from user and return string output

    #mic_list = sr.Microphone.list_microphone_names() 
    #print(mic_list)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        r.energy_threshold=150
        r.adjust_for_ambient_noise(source, duration = 1)
        print('Listening...')
        audio=r.listen(source, timeout=10)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said - {query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak("Searching Wikipedia..... Please Wait...")
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                print("According to Wikipedia")
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print("Did not find any match.. Sorry")
                speak("Did not find any match.. Sorry")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_directory = 'D:\\Music'
            songs = os.listdir(music_directory)
            # print(len(songs))
            x = random.randrange(0,len(songs),1)
            os.startfile(os.path.join(music_directory, songs[x]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The time is {strTime}\n")
            speak(f"Sir, The time is {strTime}")

        elif 'open Intellij' in query:
            codePath = "C:\\Program Files\\JetBrains\\IntelliJ IDEA 2019.1.3\\bin\\idea64.exe"
            os.startfile(codePath)

        elif 'open Pycharm' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm 2019.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'open Visual Studio' in query:
            codePath = "C:\\Users\\hites\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                if content is "None":
                    break
                to = "hiteshmunjal22@gmail.com"
                sendEmail(to, content)
                print("Email Sent")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry Sir... I am not able to send Email")
                speak("Sorry Sir... I am not able to send Email")
        elif 'quit' in query:
            speak("Bye Sir. I hope that I was upto your expectations.")
            exit()

            



    

