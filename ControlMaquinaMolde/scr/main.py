from datetime import date
#from datetime import datetime
import datetime
import csv
from Archivo.Archivo import XArchivo
from UI.VentanaPrincipal import VentanaPrincipal
from GPIO.gpio import GpioClass
from Objetos.Objeto import Objeto
from tkinter import Tk,Label,Button,Entry, Frame
root = Tk()
app = VentanaPrincipal(root) 
app.mainloop()
