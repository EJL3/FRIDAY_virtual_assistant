   #PROTOTYPE AI ASSISTANT
import pyttsx3
import speech_recognition as sr
import datetime, psutil
from playsound import playsound
import wikipedia, pywhatkit
import webbrowser
import os, PyPDF2
import weathercom
import json
import smtplib
import pyjokes
import random as rd
import pyautogui as pyi
from GoogleNews import *
import urllib3
from urllib.request import urlretrieve
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

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
        print("Command Me..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Taking command...")
        query = r.recognize_google(audio, language='en')
        print(f'User Said: {query}')

    except Exception as e:

        print("Please repeat..")
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
    server.login(your email, email pass)
    server.sendmail(your email, to, content)
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
    speak('which hour do you want the alarm to ring? ')
    alarmH = int(input("Hour:-"))
    speak('which minute')
    alarmM = int(input("Minute:-"))
    speak('A m or pm')
    amPm = str(input(" am or pm:-"))
    print("Alarm Time:", alarmH, ':', alarmM, amPm)
    speak('sir, relax. i will call you in time')
    if (amPm == "pm"):
        alarmH = alarmH + 12
    while (1 == 1):
        if (alarmH == datetime.datetime.now().hour and
                alarmM == datetime.datetime.now().minute):
            speak("sir,the time is up. i think you have to wake up")
            playsound('alarm.mp3')
            playsound('alarm.mp3')
            break

def scrnshot():
    ns = 'Fridays scrnshot.png'
    img = pyi.screenshot()
    img.save(ns)
    speak('taken screenshot,sir')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage+'percent')

    battery = psutil.sensors_battery()
    speak('battery percentage, is at')
    speak(battery.percent)

def utube():
    speak('name it sir')
    K = takeCommand()
    song = K.replace('play', '')
    speak('ok sir, kindly wait')
    pywhatkit.playonyt(song)
      
def wallpaper():
   folder = 'YOUR DIRECTORY'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    api_key = 'YOUR UNSPLASH API KEY' # Which can be found here https://unsplash.com/developers
    url = 'https://api.unsplash.com/photos/random?client_id=' + api_key  # pic from unspalsh.com
    http = urllib3.PoolManager()
    f = http.request('GET', url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    urlretrieve(photo, "YOUR DIRECTORY/a")
    subprocess.call(["killall Dock"], shell=True)
    speak('wallpaper changed successfully sir')
  
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
            vx = "https://youtube.com"
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome).open(vx)

        elif 'open google' in query:
            hx = "google.com"
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome).open(hx)

        elif 'open github' in query:
            speak('time for repositories. right sir')
            wx = "https://github.com"
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome).open(wx)

        elif 'open stack overflow' in query:
            io = "https://stackoverflow.com"
            chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome).open(io)

        if "weather report" in query:
            weather()

        elif 'alarm' in query:
            alarm()

        elif 'screenshot' in query:
            scrnshot()

        elif 'news' in query:
            News()

        if 'cpu' in query:
            cpu()

        elif 'song' in query:
            music = 'C:\\songs'
            songs = os.listdir(music)
            b = rd.choice(songs)
            print(songs)
            os.startfile(os.path.join(music, b))

        if 'story' in query:
            rate = engine.getProperty('rate')
            engine.setProperty('rate', 120)
            book = open('treasure island.pdf', 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pages = pdfReader.numPages

            for num in range(1, pages):
                page = pdfReader.getPage(num)
                text = page.extractText()
                speak(text)

        elif 'joke' in query:
            c = (pyjokes.get_joke())
            print(c)
            speak(c)
            speak('sorry,sir. i am terrible at joking')

        if 'search' in query:
            speak('what do you want to search')
            search_term = takeCommand()
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            speak('Here is what I found on google')

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        if 'coin' in query:
            moves = ["heads", "tails"]
            cmove = rd.choice(moves)
            speak("sir. the probability i got is " + cmove)
            print(cmove)

        elif 'open powerpoint' in query:
            App = 'C:/Program Files/Microsoft Office/Office15/POWERPNT.EXE'
            os.startfile(App)

        if "location" in query:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("You must be somewhere near here, as per Google maps")

        elif 'still' in query:
            speak('yes sir, at your service')

        if 'video' in query:
            utube()

        elif 'note' in query:
            speak("sir, kindly feed me what i should remember")
            Message = takeCommand()
            speak('your message was' + Message)
            remember = open('Note.txt', 'w')
            remember.write(Message)
            remember.close()

        elif 'remember' in query:
            remember = open('Note.txt', 'r')
            speak("you said" + remember.read())

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = reciever email
                sendEmail(to, content)
                speak("sir. The email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. we have a technical issue here ")

        if "game" in query:
            speak('ok sir. it would be fun')
            speak("lets play rock paper pencil. pick your choice")
            data = takeCommand()
            moves = ['rock', 'paper', 'pencil']
            cmove = rd.choice(moves)
            pmove = data
            speak("i chose" + cmove)
            speak("sir, Your choice was " + pmove)

            if pmove == cmove:
                speak("the match is draw")
            elif pmove == "pencil" and cmove == "paper":
                speak("you won the match")
            elif pmove == "paper" and cmove == "pencil":
                speak("i won the match")
            elif pmove == "rock" and cmove == "pencil":
                speak("you won the match")
            elif pmove == "rock" and cmove == "paper":
                speak("i won the match")
            elif pmove == "paper" and cmove == "rock":
                speak("you won the match")
            elif pmove == "pencil" and cmove == "rock":
                speak("i won the match")
                  
        if 'wallpaper' in query:
            wallpaper()

        if 'thank you' in query:
            speak('pleasure serving you sir!')
            exit('system shutdown')
