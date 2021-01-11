# Friday_desktop_assistant
![virtual-assistance](https://user-images.githubusercontent.com/73348960/104115741-ec69fc00-532b-11eb-9dfd-193b68521e0b.png)
Friday is a Ai assistant who takes command with your voice. As a matter of fact i have created this Pgm for the marvel iron-man fans, it does 10 to 13 command features which is controlled by your voice(cool huh?).for the most crazy part you can control your pc with your voice and make your personal desktop assistant do the job. it is not the best compared to alexa,cortana etc. but it is your self made assistant so be proud. 

# Requirements
pyttsx3 

speechRecognition

playsound

wikipedia

webbrowser

weathercom

json

SMTP

pyjokes

pyautogui

GoogleNews

And finally you need to download your desired alarm ringtone from net and name it alarm.(dont forget to convert it into 'mp3' if it is not)

# Commands
Run the pgm and say 'news' - (you can also include your sentence while giving command but it should contain the 'news' word somewhere in your phrase)

screenshot

send email

music

joke

time

open powerpoint

weather report

alarm - once you say alarm a question will arise like 'which hour' and so on. in this specific code you have to type the alarm time, i have tried to make it a voice control but the pyttsx3 only takes strings and not numerics and also cant convert a string to numeric.(if anyone knows pls share your knowledge :-})

open github

open google

open youtube

wikipedia - before commanding 'wikipedia' say some valid source infront, eg:- 'GitHub wikipedia'

saying 'thank you' will close the pgm.

# Facts
you can change the voice of the assistant by changing [0] to [1], here:- engine.setProperty('voice', voices[0].id)
you can send email to different people by just saying there name, (ALERT:- i have not included the code for this, however, you can do this by yourself by adding dictionary (take it as a challenge).
in future i will add more features to it. :-]
please keep in mind that for sending email you have to turn on less secure app access in gmail settings.
