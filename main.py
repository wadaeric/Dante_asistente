import random
import pywhatkit
from classes import SpeechModule, VoiceRecognitionModule
from datetime import datetime
from bromas import chistes


dia = datetime.now().strftime('%d')
dia_nombre = datetime.now().strftime('%A')
mes = datetime.now().strftime('%m')
mes_nombre = datetime.now().strftime('%b')
año = datetime.now().strftime('%Y')

if dia_nombre == "Monday":
    dia_nombre = "Lunes"
if dia_nombre == "Tuesday":
    dia_nombre = "Martes"
if dia_nombre == "Wednesday":
    dia_nombre = "Miercoles"
if dia_nombre == "Thursday":
    dia_nombre = "Jueves"
if dia_nombre == "Friday":
    dia_nombre = "Viernes"
if dia_nombre == "Saturday":
    dia_nombre = "Sabado"
if dia_nombre == "Sunday":
    dia_nombre = "Domingo"
    
if mes_nombre == "January":
    mes_nombre = "Enero"
if mes_nombre == "February":
    mes_nombre = "Febrero"
if mes_nombre == "March":
    mes_nombre = "Marzo"
if mes_nombre == "April":
    mes_nombre = "Abril"
if mes_nombre == "May":
    mes_nombre = "Mayo"
if mes_nombre == "June":
    mes_nombre = "Junio"
if mes_nombre == "July":
    mes_nombre = "Julio"
if mes_nombre == "August":
    mes_nombre = "Agosto"
if mes_nombre == "September":
    mes_nombre = "Septiembre"
if mes_nombre == "October":
    mes_nombre = "Octubre"
if mes_nombre == "November":
    mes_nombre = "Noviembre"
if mes_nombre == "December":
    mes_nombre = "Diciembre"


# Cargamos los modulos                
speech = SpeechModule()
recognition = VoiceRecognitionModule()

nombre = "dante"

def dar_hora():
    hora = datetime.now().strftime('%H:%M')
    return hora

def habla(text):
    speech.talk(text)
    
def cuenta_un_chiste():
    aleatorio = random.randint(1,11)
    print("chiste numero: ", aleatorio)
    habla(chistes.CHISTES[aleatorio])
    
def normaliza(string):
        # Normaliza el texto quitando acentos
        acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
        for acen in acentos:
            if acen in string:
                string = string.replace(acen, acentos[acen])
        return string
    

txt = ""
def escucha():
    global txt
    txt = ""
    try:
        # Mientras reconozca el texto
        while True:
            text = recognition.recognize()
            
            # Quitamos acentos
            text = normaliza(text)
            # Revisamos el texto
            print(text)
            
            if nombre in text:
                txt = text.replace(nombre, '')
                txt = txt.replace("oye", '')
                break
            
    except:
        pass
    return txt

def run_dante():
    while True:
        dante = escucha()
    
        # Hora
        if 'hora es' in dante:
            print("Son las "+dar_hora())
            habla("Son las "+dar_hora())
            
        # Youtube    
        elif 'reproduce' in dante:
            music = dante.replace('reproduce', '')
            music = music.replace(nombre, '')
            txt = music.replace("oye", '')
        
            print("reproduciendo "+txt)
            habla("reproduciendo "+txt)
            pywhatkit.playonyt(txt)
        # Fecha
        elif 'es hoy' in dante:
            print("Hoy es "+dia_nombre+", "+dia+" de "+mes_nombre+" del "+año)
            habla("Hoy es "+dia_nombre+", "+dia+" de "+mes_nombre+" del "+año)
            
        elif 'como estas' in dante:
            bien = "Muy bien, muchas gracias por preguntar mi amo"
            print("Muy bien, muchas gracias por preguntar mi amo")
            habla(bien)
            
        elif 'cuentame un chiste' in dante:
            cuenta_un_chiste()

        # Desconectar a Dante    
        elif 'salir' in dante:
            print("Desconectando Dante")
            habla("Desconectando Dante Asistente.")
            break
        
if __name__ == '__main__':
    run_dante()