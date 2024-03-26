from datetime import date
from datetime import datetime
import os.path as path
import csv
import os
#import keyboard
"""
clase que maneja los arhivos
crea la carpeta en caso de que no xista, define el nombre y aagrega la informacion 
"""
class XArchivo():
    #---------------------------------------regresa el turno dependiendo de la hora del dia que es
    def DameTurno(self):
        turno="desconocido"
        hoy=datetime.today()
        if hoy>=datetime(hoy.year,hoy.month,hoy.day,7,30,0,0) and hoy <=datetime(hoy.year,hoy.month,hoy.day,15,30,0,0):
            turno="_Turno1"
        if hoy>datetime(hoy.year,hoy.month,hoy.day,7,30,0,0) and hoy <=datetime(hoy.year,hoy.month,hoy.day,23,30,0,0):
            turno="_Turno2"
        if hoy>datetime(hoy.year,hoy.month,hoy.day,23,30,0,0) and hoy <datetime(hoy.year,hoy.month,hoy.day,7,30,0,0):
            turno="_Turno3"
        return turno

    def CreaCarpeta(self):
        # Crear la carpeta "archivos" en el escritorio con nombre yyyy-mm-dd_turnoX
        #obtengo la ruta del scritotio
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        #obtengo la fecha actual
        fecha_actual = datetime.now()
        #i la agrego a la ruta
        nombre_carpeta = fecha_actual.strftime("%Y-%m-%d")
        #me traigo el tueno que corresponde
        turno=self.DameTurno()
        #+ "_turnoX"
        path_carpeta = os.path.join(desktop, 'archivos', nombre_carpeta)+turno
        os.makedirs(path_carpeta, exist_ok=True)
        nombre_archivo = os.path.join(path_carpeta, 'registros.csv')
        return nombre_archivo
    #--------------------------------funcion que crear el archivo csv-------------------------------------------------------------------
    def EscribeArchivo(self, columnas):
        nombre_archivo=self.CreaCarpeta()
        if not path.exists(nombre_archivo):
            #si no existe el archivo lo crea
            with open(nombre_archivo, 'w', newline='') as file:
                #escribe la cabecera y agrega ls datos
                writer = csv.writer(file)
                writer.writerow(["operador", "atoron madera", "set up", "falla produccion", "afilado", "mtto", "automatico"])
                writer.writerow(columnas)
                file.close()
        else:
            #como existe, lo abre para agregar informacion
            with open(nombre_archivo, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(columnas)
                file.close()
    #------------------------------------------------------------------------------------------------------------------------------
