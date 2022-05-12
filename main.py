import time
from classes import SpeechModule, VoiceRecognitionModule
from datetime import datetime
import pywhatkit

# Cargamos los modulos                
speech = SpeechModule()
recognition = VoiceRecognitionModule()

nombre = "dante"

def dar_hora():
    hora = datetime.now().strftime('%H:%M')
    return hora

def habla(text):
    speech.talk(text)

def escucha():
    try:
        # Mientras reconozca el texto
        while True:
            text = recognition.recognize()
            
            # Repetira lo que se le haya dicho
            text = text.lower()
            if nombre in text:
                txt = text.replace(nombre, '')
                txt = txt.replace("oye", '')
                speech.talk(txt)
            time.sleep(1)
    except:
        pass
    return txt

def run_dante():
    dante = escucha()
    if 'hora es' in dante:
        print("Son las "+dar_hora())
        habla("Son las "+dar_hora())
        
    if 'reproduce' in dante:
        music = dante.replace('reproduce', '')
        print('reproduciendo'+music)
        habla('reproduciendo'+music)
        pywhatkit.playonyt(music)
        
if __name__ == '__main__':
    run_dante()