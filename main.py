import speech_recognition as sr

r=sr.Recognizer()

def recordAudio():
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

print("hey!!")
voice_data=recordAudio()
print(voice_data)
