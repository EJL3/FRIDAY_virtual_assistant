import pyttsx3
import speech_recognition as sr
import datetime
from playsound import playsound
import wikipedia
import webbrowser
import os
import weathercom
import json
import smtplib
import pyjokes
import random as rd
import pyautogui as pyi
from GoogleNews import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("hello sir, friday here. how can I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("what should i do sir?")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Taking command...")
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}\n")

    except Exception as e:

        speak("i didn't get you, sir")
        return "None"
    return query

def News():
    gln = GoogleNews()
    gln = GoogleNews('en')
    gln.search('india')
    gln.getpage(1)
    gln.result()
    o = gln.gettext()
    print(o)
    speak(o)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'email password')
    server.sendmail('your email', to, content)
    server.close()

def weather():
    speak('which city, sir.')
    city = takeCommand()
    weatherDetails = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
    temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
    phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
    print('humidity =', humidity)
    print('temperature =', temp,'c')
    print('climate', phrase)
    speak('report from'+str(city)+'sir')
    speak('humidity'+str(humidity))
    speak('temperature'+str(temp)+'degree celsius')
    speak('climate'+str(phrase))

def alarm():
    speak('set your time')
    alarmH = int(input("What hour do you want the alarm to ring? "))
    alarmM = int(input("What minute do you want the alarm to ring? "))
    amPm = str(input("am or pm? "))
    print("Alarm Time:", alarmH, alarmM, amPm)
    speak('sir, relax. i will call you in time')
    if (amPm == "pm"):
        alarmH = alarmH + 12
    while (1 == 1):
        if (alarmH == datetime.datetime.now().hour and
                alarmM == datetime.datetime.now().minute):
            speak("sir,the time is up. i think you have to wake up")
            playsound('(put directory):/alarm.mp3')
            playsound('(put directory):/alarm.mp3')
            break

def scrnshot():
    ns = 'give a directory where you want to store screenshots'
    img = pyi.screenshot()
    img.save(ns)
    speak('taken screenshot,sir')

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            vx = "youtube.com"
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome).open(vx)

        elif 'open google' in query:
            speak('launching search engine')
            hx = "google.com"
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome).open(hx)

        elif 'github' in query:
            wx = "github.com"
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome).open(wx)

        if "weather report" in query:
            weather()

        elif "alarm" in query:
            alarm()

        elif 'screenshot' in query:
            scrnshot()

        elif 'news' in query:
            News()

        elif 'music' in query:
            music = 'directory of your music folder'
            songs = os.listdir(music)
            b = rd.choice(songs)
            print(songs)
            os.startfile(os.path.join(music, b))

        elif 'joke' in query:
            c = (pyjokes.get_joke())
            print(c)
            speak(c)
            speak('sorry,sir. i am terrible at joking')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open powerpoint' in query:
            App = 'C:/Program Files/Microsoft Office/Office15/POWERPNT.EXE'
            os.startfile(App)

        elif ' send email ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'email of the person you want to send message'
                sendEmail(to, content)
                speak("sir. The email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. I am not able to send this email")

        if 'thank you' in query:
            speak('pleasure serving you sir!')
            exit('system shutdown')
