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
        print("yes")
        location=recordAudio("where you want to go??")
        url='https://google.nl/maps/place/'+location+'/&amp'
        webbrowser.get().open(url)
        print("you are going to="+location)


voice_data=recordAudio('hello dude!! how can I you? ')
respond(voice_data)
