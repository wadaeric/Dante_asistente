import pyttsx3, platform, requests
import speech_recognition as sr
from datetime import datetime

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
        if so == "Linux":
            voice_id = 'spanish'
            self.engine.setProperty('voice', voice_id)
        else:
            self.engine.setProperty('voice', voices[1].id)
        
    def talk(self, text):
        
        # Dice en voz alta el texto que se le ha pasado
        self.engine.say(text)
        # Se ejecuta y espera
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
                
                # Formatamos el texto a minisculas
                text = text.lower()                
                
                return text
            except:
                return None
            
class Tiempo:
    def __init__(self, key="1cd68cbda9a67ad286e634983480ba0f"):
        # Ubicacion donde queremos saber el clima
        sitio = "Tavernes de la Valldigna"

        # url para extraer los datos
        url_tiempo = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric&lang=es".format(sitio,key)

        self.res = requests.get(url_tiempo)

        # volcamos los datos en formato json y los almacenamos con esta variable
        self.datos = self.res.json()
        
    def temperatura(self):
        # Extraemos la temperatura en Boolean
        temp = self.datos["main"]["temp"]
        # Tranformamos en String
        temp = str(temp)
        return temp
    
    def desc(self):
        # Obtenemos la descripcion meteorologica
        descripcion = self.datos["weather"][0]["description"]
        return descripcion
    
class FechaHora:
    def __init__(self):
        
        self.dia = datetime.now().strftime('%d')
        self.dia_nombre = datetime.now().strftime('%A')
        self.mes = datetime.now().strftime('%m')
        self.mes_nombre = datetime.now().strftime('%b')
        self.año = datetime.now().strftime('%Y')

        if self.dia_nombre == "Monday":
            self.dia_nombre = "Lunes"
        if self.dia_nombre == "Tuesday":
            self.dia_nombre = "Martes"
        if self.dia_nombre == "Wednesday":
            self.dia_nombre = "Miercoles"
        if self.dia_nombre == "Thursday":
            self.dia_nombre = "Jueves"
        if self.dia_nombre == "Friday":
            self.dia_nombre = "Viernes"
        if self.dia_nombre == "Saturday":
            self.dia_nombre = "Sabado"
        if self.dia_nombre == "Sunday":
            self.dia_nombre = "Domingo"
            
        if self.mes_nombre == "January":
            self.mes_nombre = "Enero"
        if self.mes_nombre == "February":
            self.mes_nombre = "Febrero"
        if self.mes_nombre == "March":
            self.mes_nombre = "Marzo"
        if self.mes_nombre == "April":
            self.mes_nombre = "Abril"
        if self.mes_nombre == "May":
            self.mes_nombre = "Mayo"
        if self.mes_nombre == "June":
            self.mes_nombre = "Junio"
        if self.mes_nombre == "July":
            self.mes_nombre = "Julio"
        if self.mes_nombre == "August":
            self.mes_nombre = "Agosto"
        if self.mes_nombre == "September":
            self.mes_nombre = "Septiembre"
        if self.mes_nombre == "October":
            self.mes_nombre = "Octubre"
        if self.mes_nombre == "November":
            self.mes_nombre = "Noviembre"
        if self.mes_nombre == "December":
            self.mes_nombre = "Diciembre"
            
    def dar_hora(self):
        hora = datetime.now().strftime('%I:%M')
        return hora
    
    def dar_fecha(self):
        fecha = "Hoy es "+self.dia_nombre+", "+self.dia+" de "+self.mes_nombre+" del "+self.año
        return fecha