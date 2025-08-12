import os

import speech_recognition as sr

def speech_tr():

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Bir şey söyle!")
        audio = r.listen(source)


    text = r.recognize_google(audio, language="tr-TR")
    return text 

def speech_eng():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)


    text = r.recognize_google(audio, language="tr-TR")
    return text 