import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("hey!! say something")
    audio=r.listen(source)
    voiceData=r.recognize_google(audio)
    print(voiceData)