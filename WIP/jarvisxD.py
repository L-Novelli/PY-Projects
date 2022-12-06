import pyttsx3 #voice engine import
import datetime
import speech_recognition as sr

engine = pyttsx3.init()


def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().date)
    speak(year)
    speak(month)
    speak(date)


def wishme(): 
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    elif hour >= 18 and hour < 24:
        speak("Good night")
    speak("I'm at your service")

wishme()

#def voiceCommand():
 #   r = sr.Recognizer()
#    with sr.Microphone() as source:
#        print("Estoy escuchando . . .")
#        r.pause_threshold = 1
 #       audio = r.listen(source)

 #   try:
 #       print("Reconociendo . . .")
 #       query = r.recognize_google(audio, language='en-in')
 #       print(query)

 #   except Exception as e:
 #       print(e)
 #       speak("Por favor repeti lo que dijiste")

  #      return "None"
    
 #   return query
