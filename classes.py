import pyttsx3
import speech_recognition as sr
import platform






# Voz del asistente
class SpeechModule:
    def __init__(self):
        # Controlador para el sistema operativo Windows: sapi5
        self.engine = pyttsx3.init("sapi5")
        
        # Establecemos la velocidad del habla en 125
        self.engine.setProperty('rate', 125)
        # El volumen va de 0.0 a 1.0 es bool
        self.engine.setProperty('volume', 1)
        
        voices = self.engine.getProperty('voices')
        # Asignamos la voz numero 0
        self.engine.setProperty('vocie', voices[0].id)
        
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Reconocimiento de voz de Google
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
                text = self. r.recognize_google(audio, key=self.key, language="es")
                return text
            except:
                return None