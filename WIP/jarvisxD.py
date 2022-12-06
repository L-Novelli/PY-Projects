import pyttsx3 #voice engine import
import datetime
import speech_recognition as sr


engine = pyttsx3.init()


def speak (audio):
    engine.say(audio)
    engine.runAndWait()
  
  
speak("Hola, soy Ela. Su asistente personal.")

def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().date)
    speak(year)
    speak(month)
    speak(date)


def wishme():
    speak("Bienvenido")
    speak("la hora actual es:")
    time()   
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Buen dia")
    elif hour >= 12 and hour < 18:
        speak("Buenas tardes")
    elif hour >= 18 and hour < 24:
        speak("Buenas noches")
    speak("Estoy a tu servicio")

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
