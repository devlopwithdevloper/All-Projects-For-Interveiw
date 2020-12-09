import pyttsx3 
from pyttsx3 import *
import datetime
import speech_recognition as sr
from speech_recognition import *
import wikipedia
from wikipedia import *
import webbrowser
import os

#Defining global engine
#global variables

global engine
global sys_voices
global Jarvis_Voice

#Defining Jarvis Default Voice 

Jarvis_Voice ='Microsoft Server Speech Text to Speech Voice (en-US, ZiraPro)'

#Initialising Jarvis Voice For Speaking

engine = pyttsx3.init('sapi5')
sys_voices = engine.getProperty('voices')
if str(sys_voices[0].name) == Jarvis_Voice:
    engine.setProperty('voice',sys_voices[0].id)
    

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def Wish():
    time = int(datetime.now().hour)
    if time >= 0 and time < 12:
            Speak('good  morning')
            
    elif time >= 12 and time < 16:
           Speak('good   afternoon')
           
    elif time >= 17 and time < 20:
            Speak('good  evening')
            
    else:
        engine.say('good   night')
        engine.runAndWait()
    Speak('Hello I am Jarvis,How Can I Help You')

def Listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 5) as source:
        print('Listening....')
        r.adjust_for_ambient_noise(source=source)
        mic_input = r.listen(source=source)
    try:
        print('recognizing')
        query = r.recognize_google(mic_input,language = 'en-in')
    except RequestError:
        print("Can't Connect Please Check Your Connection")
        Speak("Can't Connect Please Check Your Connection")
        query = 'None'
    except UnknownValueError:
        print("Can't Understand")
        query = 'None'
    return query

#-------------------------------------Our  Code Starts From Here---------------------------------------- 
Wish()
while True:
    UserCommand = Listen().lower()
    if 'wikipedia' in UserCommand:
        UserCommand = UserCommand.replace('wikipedia','')
        results = wikipedia.summary(UserCommand,sentences = 10)
        Speak('According To Wikipedia')
        Speak(results)
    
    elif 'open whatsapp' in UserCommand:
        UserCommand = UserCommand.strip('open')
        try:
            webbrowser.open_new_tab(str(UserCommand+'.com'))
        except Exception as error:
            Speak("Can't open Whatsapp")
    
    elif 'open youtube' in UserCommand:
        try:
            webbrowser.open('youtube.com')
        except Exception as error:
           
            Speak("Can't Open Youtube")
    
    elif 'open my code editor' in UserCommand:
        Speak('Okay')
    
    elif 'open website'in UserCommand:
        UserCommand = UserCommand.strip('open website')
        try:
            webbrowser.open_new_tab(str(UserCommand))
        except Exception as error:
            Speak("This Site Can't Be Reached")
    



