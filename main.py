import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import os # to remove created audio files

class person:
    name = ''
    def setName(self, name):
        self.name = name

class assistant:
    def __init__(self,name):
        self.name=name
    def setName(self,name):
        self.name=name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:

askt=False

def record_audio(ask=False):
    with sr.Microphone(sample_rate = 48000,chunk_size = 2048) as source: # microphone as source

        global askt

        if ask:
            if  ("or you want to give me a nickname" in ask) and (askt==False):
                askt=True
                speak(ask)
            if ("or you want to give me a nickname" not in ask) and (askt==True):
                speak(ask)

        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f">> {voice_data.lower()}") # print what user said
        return voice_data.lower()


# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(f"{assistant_obj.name}: {audio_string}") # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    
    # Just starting
    if there_exists(['yes','yep','yeah','yeah offcourse','yes offcourse','yes i want']):
        vd=record_audio("so what nickname you want to give me")
        assistant_name = vd.split("is")[-1].strip()    
        speak(f"okay, now my nickname is  {assistant_name}")
        assistant_obj.setName(assistant_name)#remember assistant nickname
        pd=record_audio("and what is your name")
        person_name = pd.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    if there_exists(['no','naa','nah']):
        pd=record_audio("so what is your name")
        person_name = pd.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)

    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    if there_exists(["how are you","how are you doing","how's you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")


    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak(f"my name is {assistant_obj.name}")
    
    if there_exists(['i want to change your nickname','want to change your name',\
        'want to change your niknamename','i want to change your nickname']):
        vd=record_audio("so what nickname you want to give me")
        assistant_name = vd.split("is")[-1].strip()    
        speak(f"okay, now my nickname is  {assistant_name}")
        assistant_obj.setName(assistant_name)#remember assistant nickname
         
    # 3: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 4: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 5: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
    
     #6 weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        speak("Here is what I found for on google")
     

     #7 stone paper scisorrs
    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        cmove=random.choice(moves)
        pmove=voice_data
        

        speak("The computer chose " + cmove)
        speak("You chose " + pmove)
        
        if pmove==cmove:
            speak("the match is draw")
        elif pmove== "rock" and cmove== "scissor":
            speak("Player wins")
        elif pmove== "rock" and cmove== "paper":
            speak("Computer wins")
        elif pmove== "paper" and cmove== "rock":
            speak("Player wins")
        elif pmove== "paper" and cmove== "scissor":
            speak("Computer wins")
        elif pmove== "scissor" and cmove== "paper":
            speak("Player wins")
        elif pmove== "scissor" and cmove== "rock":
            speak("Computer wins")

     #8 toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        speak("The computer chose " + cmove)

     #9 calc
    if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            speak("Wrong Operator")

     #10: exiting
    if there_exists(['exit','goodby','quit','leave me alone']):
        speak(f"goodby {person_obj.name}")
        exit()



time.sleep(1)

person_obj = person()
assistant_obj=assistant('Malena')

while(1):
    voice_data = record_audio(f"hey you can call me  {assistant_obj.name}  or you want to give me a nickname") # get the voice input
    respond(voice_data) # respond
