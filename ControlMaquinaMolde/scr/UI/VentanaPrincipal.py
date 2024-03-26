from datetime import date
from datetime import datetime
import time
import  tkinter
from tkinter.font import Font
from tkinter import Tk,Label,Button,Entry, Frame
from pynput import keyboard as kb
from Archivo.Archivo import XArchivo

class VentanaPrincipal(Frame):
    #-------------------------------------------------------------------------------Constructor-----------------------------------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master,width=1000, height=500)
        self.master = master
        self.pack()
        self.create_widgets()
        self.limpiaDatos()
        self.Inicializateclado()
        self.peridoOperador=datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0,0)
        self.peridoAtoronMadera=datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0,0)
        self.peridoSetup=datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0,0)
        self.peridoFallaProduccion=datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0,0)
        self.peridoAfilado=datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0,0)
        self.peridoMtto=datetime(datetime.now().year,datetime.now().month,datetime.now().day,0,0,0,0)
        
    #------------------------------------------------Crea la interfac grafica-----------------------------------------------------------------------------------------------------------------------------
    def create_widgets(self):
        #----------------------Ventana-------------------------------
        self.master.title("MEDIDOR DE TIEMPOS")
        self.master.geometry("1000x500")
        self.master.resizable(0,0) #no se permite cambiar el tamaño de la ventana
        #definimos una fuente
        fuente=Font( size=14)
        # etiqueta
        py=50
        dy=35
        tkinter.Label(self,text="MEDIDOR DE TIEMPOS",font=fuente).place(x=300,y=1) 
        #tkinter.Label(ventana,text="OPERADOR           PULSA TECLA 1               TIEMPO PERIODO OPERADOR",font=fuente).place(x=10,y=50) 
        tkinter.Label(self,text="OPERADOR",font=fuente).place(x=10,y=py) 
        self.label1=tkinter.Label(self,text="PULSA TECLA 1",font=fuente)
        self.label1.place(x=300,y=py) 
        self.labelPeriodoOperador=tkinter.Label(self,text="TIEMPO PERIODO OPERADOR",font=fuente)
        self.labelPeriodoOperador.place(x=600,y=py) 
        py=py+dy 

        tkinter.Label(self,text="ATORON MADERA",font=fuente).place(x=10,y=py)
        self.label2=tkinter.Label(self,text="PULSA TECLA 2",font=fuente)
        self.label2.place(x=300,y=py)
        self.labelPeriodoAtoronMadera=tkinter.Label(self,text="TIEMPO ATORON MADERA",font=fuente)
        self.labelPeriodoAtoronMadera.place(x=600,y=py) 
        py=py+dy 

        tkinter.Label(self,text="SETUP",font=fuente).place(x=10,y=py)
        self.label3=tkinter.Label(self,text="PULSA TECLA 3",font=fuente)
        self.label3.place(x=300,y=py)
        self.labelPeriodoSetup=tkinter.Label(self,text="TIEMPO SETUP",font=fuente)
        self.labelPeriodoSetup.place(x=600,y=py) 
        py=py+dy 

        tkinter.Label(self,text="FALLA PRODUCCION",font=fuente).place(x=10,y=py)
        self.label4=tkinter.Label(self,text="PULSA TECLA 4",font=fuente)
        self.label4.place(x=300,y=py)
        self.labelPeriodoFallaProduccion=tkinter.Label(self,text="TIEMPO FALLA PRODUCCION",font=fuente)
        self.labelPeriodoFallaProduccion.place(x=600,y=py) 
        py=py+dy 

        tkinter.Label(self,text="AFILADO",font=fuente).place(x=10,y=py)
        self.label5=tkinter.Label(self,text="PULSA TECLA 5",font=fuente)
        self.label5.place(x=300,y=py)
        self.labelPeriodoAfilado=tkinter.Label(self,text="TIEMPO AFILADO",font=fuente)
        self.labelPeriodoAfilado.place(x=600,y=py) 
        py=py+dy 

        tkinter.Label(self,text="MTTO",font=fuente).place(x=10,y=py)
        self.label6=tkinter.Label(self,text="PULSA TECLA 6",font=fuente)
        self.label6.place(x=300,y=py)
        self.labelPeriodoMtto=tkinter.Label(self,text="TIEMPO MTTO",font=fuente)
        self.labelPeriodoMtto.place(x=600,y=py) 
        py=py+dy 

        tkinter.Label(self,text="AUTOMATICO",font=fuente).place(x=10,y=py)
        tkinter.Label(self,text="TECLA 8 NO SE PUEDE",font=fuente).place(x=300,y=py)
        tkinter.Label(self,text="TIEMPO TRABAJADO EN    ",font=fuente).place(x=600,y=py)
        py=py+dy 

        tkinter.Label(self,text="PULSAR ESTA TECLA",font=fuente).place(x=300,y=py)
        tkinter.Label(self,text="AUTOMATICO",font=fuente).place(x=600,y=py)
        py=py+dy 

        tkinter.Label(self,text="TECLA MAL",font=fuente).place(x=10,y=py)
        tkinter.Label(self,text="PULSA TECLA 9",font=fuente).place(x=300,y=py)
        py=py+dy 

        tkinter.Label(self,text="PRESIONADA",font=fuente).place(x=10,y=py)
        
    #-------------------------------------------------------------Inicializa el teclado------------------------------------------------------------------------------------------------------------
    def Inicializateclado(self):
        escuchador = kb.Listener(self.onKeyPress)
        escuchador.start()
    #---------------------------------------------------------Detecta la tecla pulsada-------------------------------------------------------------------------------------------------------------
    def onKeyPress(self,tecla):
        try:
            self.horaInicial= datetime.now()
            #self.tiempoInicial=time.time()
            if tecla==kb.KeyCode.from_char('1'):
                self.limpiaDatos()
                self.operador=self.horaInicial.strftime("%H:%M:%S")
                self.label1.config(fg="green")
            if tecla==kb.KeyCode.from_char('2'):
                self.limpiaDatos()
                self.atoronMadera=self.horaInicial.strftime("%H:%M:%S")
                self.label2.config(fg="green")
            if tecla==kb.KeyCode.from_char('3'):
                self.limpiaDatos()
                self.setup=self.horaInicial.strftime("%H:%M:%S")
                self.label3.config(fg="green")
            if tecla==kb.KeyCode.from_char('4'):
                self.limpiaDatos()
                self.fallaProduccion=self.horaInicial.strftime("%H:%M:%S")
                self.label4.config(fg="green")
            if tecla==kb.KeyCode.from_char('5'):
                self.limpiaDatos()
                self.afilado=self.horaInicial.strftime("%H:%M:%S")
                self.label5.config(fg="green")
            if tecla==kb.KeyCode.from_char('6'):
                self.limpiaDatos()
                self.mtto=self.horaInicial.strftime("%H:%M:%S")
                self.label6.config(fg="green")
            if tecla==kb.KeyCode.from_char('p'):
                #en este caso se simula que se detecto el funcionamiento del pin12 y se guarda el valor enel archivo
                time.sleep(.1)
                self.horaFinal=datetime.now()
                #self.tiempoFinal=time.time()
                self.automatico=self.horaFinal.strftime("%H:%M:%S")
                self.datos=[self.operador,self.atoronMadera,self.setup,self.fallaProduccion,self.afilado,self.mtto,self.automatico]
                archivo=XArchivo()
                archivo.EscribeArchivo(self.datos)
                self.MuestraTiempos()
                self.limpiaDatos()
        except Exception as err:
            print(f"ocurrio un error {err=}, {type(err)=}")    
    
    #-----------------------Limpia los datos-------------------------------------------------------------------------------------
    def limpiaDatos(self):
        self.operador=""
        self.atoronMadera=""
        self.setup=""
        self.fallaProduccion=""
        self.afilado=""
        self.mtto=""
        self.automatico=""
        #qito el color
        self.label1.config(fg="black")
        self.label2.config(fg="black")
        self.label3.config(fg="black")
        self.label4.config(fg="black")
        self.label5.config(fg="black")
        self.label6.config(fg="black")
        
    def MuestraTiempos(self):        
        if self.operador!="":
            #ha cambiado el tiempo
            inicio=datetime.strptime(self.operador,"%H:%M:%S")
            final=datetime.strptime(self.automatico,"%H:%M:%S")
            self.peridoOperador+=final-inicio
            texto="TIEMPO PERIODO OPERADOR: "+self.peridoOperador.strftime("%H:%M:%S")
            self.labelPeriodoOperador.config(text=texto)
        if self.atoronMadera!="":
            #ha cambiado el tiempo
            inicio=datetime.strptime(self.atoronMadera,"%H:%M:%S")
            final=datetime.strptime(self.automatico,"%H:%M:%S")
            self.peridoAtoronMadera+=final-inicio
            texto="TIEMPO ATORON MADERA: "+self.peridoAtoronMadera.strftime("%H:%M:%S")
            self.labelPeriodoAtoronMadera.config(text=texto)
        if self.setup!="":
            #ha cambiado el tiempo
            inicio=datetime.strptime(self.setup,"%H:%M:%S")
            final=datetime.strptime(self.automatico,"%H:%M:%S")
            self.peridoSetup+=final-inicio
            texto="TIEMPO SETUP: "+self.peridoSetup.strftime("%H:%M:%S")
            self.labelPeriodoSetup.config(text=texto)
        if self.fallaProduccion!="":
            #ha cambiado el tiempo
            inicio=datetime.strptime(self.fallaProduccion,"%H:%M:%S")
            final=datetime.strptime(self.automatico,"%H:%M:%S")
            self.peridoFallaProduccion+=final-inicio
            texto="TIEMPO FALLA PRODUCCION: "+self.peridoFallaProduccion.strftime("%H:%M:%S")
            self.labelPeriodoFallaProduccion.config(text=texto)
        if self.afilado!="":
            #ha cambiado el tiempo
            inicio=datetime.strptime(self.afilado,"%H:%M:%S")
            final=datetime.strptime(self.automatico,"%H:%M:%S")
            self.peridoAfilado+=final-inicio
            texto="TIEMPO AFILADO: "+self.peridoAfilado.strftime("%H:%M:%S")
            self.labelPeriodoAfilado.config(text=texto)
        if self.mtto!="":
            #ha cambiado el tiempo
            inicio=datetime.strptime(self.mtto,"%H:%M:%S")
            final=datetime.strptime(self.automatico,"%H:%M:%S")
            self.peridoMtto+=final-inicio
            texto="TIEMPO MTTO: "+self.peridoMtto.strftime("%H:%M:%S")
            self.labelPeriodoMtto.config(text=texto)
    