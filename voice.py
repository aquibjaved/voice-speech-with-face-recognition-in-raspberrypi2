import speech_recognition as sr
import subprocess,sys
import pyttsx,time

#speech setting
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)


#obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    engine.say("say the name which you want to save")
    engine.runAndWait()
    audio = r.listen(source)
    

#recognize speech using Google Speech Recognition
try:
    speech = (r.recognize_google(audio))
    print speech
    import sys
    sys.argv=['create_train.py',speech]
    execfile('create_train.py')
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


