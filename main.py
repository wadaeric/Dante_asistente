import random, pywhatkit, time
from classes import SpeechModule, VoiceRecognitionModule, Tiempo, FechaHora
from bromas import chistes


# Cargamos los modulos                
speech = SpeechModule()
recognition = VoiceRecognitionModule()
tiempo = Tiempo()
fechahora = FechaHora()

nombre = "dante"
    
def cuenta_un_chiste():
    aleatorio = random.randint(1,11)
    print("chiste numero: ", aleatorio)
    speech.talk(chistes.CHISTES[aleatorio])
    
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
            time.sleep(1)
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
            hora = fechahora.dar_hora()
            print("Son las "+hora)
            speech.talk("Son las "+hora)
            
        # Fecha
        elif 'es hoy' in dante:
            fecha = fechahora.dar_fecha()
            print(fecha)
            speech.talk(fecha)
            
        # Youtube
        elif 'reproduce' in dante:
            music = dante.replace('reproduce', '')
            music = music.replace(nombre, '')
            txt = music.replace("oye", '')
        
            print("reproduciendo "+txt)
            speech.talk("reproduciendo "+txt)
            pywhatkit.playonyt(txt)
            
        # Como estas
        elif 'como estas' in dante:
            bien = "Muy bien, muchas gracias por preguntar mi amo"
            print(bien)
            speech.talk(bien)
            
        # Gracias
        elif 'gracias' in dante:
            nada = "De nada mi amo, es un placer poder ayudarle"
            print(nada)
            speech.talk(nada)
        
        # Cuenta un chiste
        elif 'chiste' in dante:
            cuenta_un_chiste()
            
        # Tiempo
        elif 'tiempo' in dante:
            lugar = "Tavèrnes de la Valldigna"
            descripcion = tiempo.desc()
            temp = tiempo.temperatura()
            print("hoy en "+lugar+" hace un día con "+descripcion+", Con una temperatura de "+temp+" grados")
            speech.talk("hoy en "+lugar+" hace un día con "+descripcion+", con una temperatura de "+temp+" grados")

        # Desconectar a Dante
        elif 'salir' in dante:
            print("Desconectando Dante")
            speech.talk("Desconectando Dante Asistente.")
            break
        
if __name__ == '__main__':
    run_dante()