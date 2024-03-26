from datetime import date
from datetime import datetime
import csv
from Archivo.Archivo import XArchivo
from UI.VentanaPrincipal import VentanaPrincipal
from tkinter import Tk,Label,Button,Entry, Frame
#import time
#string=datetime.now().strftime("%H:%M:%S")
#print(string)
#fecha = datetime.strptime(string,"%H:%M:%S")
#print(fecha) 
"""
inicio = datetime.now()
time.sleep(.001)
fin = datetime.now()
print(fin-inicio) # 1.0005340576171875
"""

"""
archivo=XArchivo()
datos = ["10", "20", "30", "40", "50", "60", "70"]
archivo.EscribeArchivo(datos)
"""
root = Tk()
app = VentanaPrincipal(root) 
app.mainloop()

"""
with open('d:/PROYECTOS/Python/holamundo/eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['operador','atoron madera','set up','falla produccion','afilado','mtto','automatico'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    
print("hola oscar")
munero1=10
numero2=201
numero3=munero1+numero2
print("la suma es", numero3)
"""
"""
hoy=datetime.today()
fecha=datetime(hoy.year,hoy.month,hoy.day,5,30,0,0)
#hoy.h//
print(hoy, fecha)
"""