import pyttsx3
import speech_recognition as sr
import platform

so = platform.system()

if so == "Windows":
    controlador = "sapi5"
elif so == "Linux":
    controlador = "espeak"
else:
    # MAC OS
    controlador = "nsss"

# Voz del asistente
class SpeechModule:
    def __init__(self):
        
        # Controlador para el sistema operativo
        self.engine = pyttsx3.init(controlador)
        
        # Establecemos la velocidad del habla en 175 para que hable rapido
        self.engine.setProperty('rate', 175)
        
        # El volumen va de 0.0 a 1.0 es bool
        self.engine.setProperty('volume', 1)
        
        voices = self.engine.getProperty('voices')
        # Asignamos la voz numero 1
        self.engine.setProperty('voice', voices[1].id)
        
    def talk(self, text):
        
        self.engine.say(text)
        self.engine.runAndWait()

# Reconocimiento de voz
class VoiceRecognitionModule:
    def __init__(self, key=None):
        
        # En caso de ser software comercial se tiene que pagar una key
        self.key = key
        self.r = sr.Recognizer()
       
    def recognize(self):
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = self.r.listen(source)
            try:
                text = self. r.recognize_google(audio, key=self.key, language="ES-es")
                
                text = text.lower()                
                
                return text
            except:
                return None