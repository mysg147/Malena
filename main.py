import speech_recognition as sr
import webbrowser

r=sr.Recognizer()

def recordAudio(ask=False):
    if(ask):
        print(ask)
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("unknown value ")
        except sr.RequestError:
            print("request error")
        return voice_data
def respond(voice_data):
    if "what is your name" in voice_data:
        print("my name is shubham")
    
    if "search" in voice_data:
        
        search=recordAudio("what do you want to search.......")
        url="https://google.com/search?q="+search
        webbrowser.get().open(url)
        print("here i found for your search="+search)
        
    if "maps" in voice_data:
        print("yes")import speech_recognition as sr
import webbrowser
import time
from time import ctime
import playsound
import os
from gtts import gTTS
import random

r=sr.Recognizer()

def recordAudio(ask=False):
    if(ask):
        anebelle_speak(ask)
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            anebelle_speak("unknown value ")
        except sr.RequestError:
            anebelle_speak("request error")
        return voice_data

def respond(voice_data):
    if "what is your name" in voice_data:
        anebelle_speak("my name is anebelle")
    
    if "search" in voice_data:
        
        search=recordAudio("what do you want to search")
        url="https://google.com/search?q="+search
        webbrowser.get().open(url)
        anebelle_speak("here i found for your search="+search)
        
    if "map" in voice_data:
        anebelle_speak("yes")
        location=recordAudio("where you want to go??")
        url='https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        anebelle_speak("here i found your location="+location)
    
    if "exit" in voice_data:
        anebelle_speak("Exiting")
        exit()

def anebelle_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)

while(True):
    voice_data=recordAudio('hello dude how can I help you')
    respond(voice_data)

        location=recordAudio("where you want to go??")
        url='https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        print("you are going to="+location)


voice_data=recordAudio('hello dude!! how can I you? ')
respond(voice_data)
