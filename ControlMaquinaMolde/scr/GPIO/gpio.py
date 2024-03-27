import RPi.GPIO as GPIO
#la libreria para el control de los pines es "pip3 install rpi.gpio"
#si no funciona ese comando hay que intentarlo on este
#sudo apt install python3-rpi.gpio

#clase que se encarga de trabajar con los pines de las rapberry
class GpioClass():
    #-------------------------------------------------------Constructor-------------------------------------------------------------
    def __init__(self):
        try:
            #se inicializa los pines que se nececiten
            self.Pin12=12
            GPIO.cleanup()
            #confoguro los pines
            GPIO.setmode(GPIO.BOARD)
            #se configura el pin 12 como entrada
            GPIO.setup(self.Pin12,GPIO.IN)
        except Exception as err:        
            print(f"ocurrio un error en GpioClass:__init__ {err=}, {type(err)=}")    
    #-------------------------------------------------------maquinaStatus-------------------------------------------------------------
    def maquinaStatus(self):
        try:
            #regresa el estatus de la maquina
            valor=GPIO.input(self.Pin12)
            #valor=1
            return valor
        except Exception as err:        
            print(f"ocurrio un error en GpioClass:maquinaStatus {err=}, {type(err)=}")    
