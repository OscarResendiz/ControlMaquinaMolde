import RPi.GPIO as GPIO
import time
import pathlib
pin=7
boton=12
directorio=pathlib.Path.home()/'Desktop'
print("directorio=",directorio)
#GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
GPIO.setup(boton,GPIO.IN)
conteo=0
valor=GPIO.input(boton)
print("boton=",valor)
while conteo<1:
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    conteo+=1
GPIO.cleanup()
print("hola")
#la libreria para el control de los pines es "pip3 install rpi.gpio"
#si no funciona ese comando hay que intentarlo on este
#sudo apt install python3-rpi.gpio