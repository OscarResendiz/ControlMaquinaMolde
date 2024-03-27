from datetime import date
from datetime import datetime
import time
import  tkinter
from tkinter.font import Font
from tkinter import Tk,Label,Button,Entry, Frame
from pynput import keyboard as kb
from Archivo.Archivo import XArchivo
from GPIO.gpio import GpioClass
from Objetos.Objeto import Objeto
class VentanaPrincipal(Frame):
    #-------------------------------------------------------------------------------Constructor-----------------------------------------------------------------------------------------------------------
    def __init__(self, master=None):
        super().__init__(master,width=1000, height=500)
        self.master = master
        self.pack()
        self.Objetos=[Objeto("TIEMPO PERIODO OPERADOR: ",'1'),Objeto("TIEMPO ATORON MADERA: ",'2'),Objeto("TIEMPO SETUP: ",'3'),Objeto("TIEMPO FALLA PRODUCCION: ",'4'),Objeto("TIEMPO AFILADO: ",'5'),Objeto("TIEMPO MTTO: ",'6'),Objeto("TIEMPO TRABAJADO: ",'p')]
        self.create_widgets()
        self.Inicializateclado()
        self.gpio=GpioClass()
        self.activo=False #por default la maquina esta en funcionamiento
        self.timer1()
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
        tkinter.Label(self,text="OPERADOR",font=fuente).place(x=10,y=py) 
        self.label1=tkinter.Label(self,text="PULSA TECLA 1",font=fuente)
        self.label1.place(x=300,y=py) 
        self.labelPeriodoOperador=tkinter.Label(self,text="TIEMPO PERIODO OPERADOR",font=fuente)
        self.labelPeriodoOperador.place(x=600,y=py) 
        self.Objetos[0].setLables(self.labelPeriodoOperador,self.label1)
        py=py+dy 

        tkinter.Label(self,text="ATORON MADERA",font=fuente).place(x=10,y=py)
        self.label2=tkinter.Label(self,text="PULSA TECLA 2",font=fuente)
        self.label2.place(x=300,y=py)
        self.labelPeriodoAtoronMadera=tkinter.Label(self,text="TIEMPO ATORON MADERA",font=fuente)
        self.labelPeriodoAtoronMadera.place(x=600,y=py) 
        self.Objetos[1].setLables(self.labelPeriodoAtoronMadera,self.label2)
        py=py+dy 

        tkinter.Label(self,text="SETUP",font=fuente).place(x=10,y=py)
        self.label3=tkinter.Label(self,text="PULSA TECLA 3",font=fuente)
        self.label3.place(x=300,y=py)
        self.labelPeriodoSetup=tkinter.Label(self,text="TIEMPO SETUP",font=fuente)
        self.labelPeriodoSetup.place(x=600,y=py) 
        self.Objetos[2].setLables(self.labelPeriodoSetup,self.label3)
        py=py+dy 

        tkinter.Label(self,text="FALLA PRODUCCION",font=fuente).place(x=10,y=py)
        self.label4=tkinter.Label(self,text="PULSA TECLA 4",font=fuente)
        self.label4.place(x=300,y=py)
        self.labelPeriodoFallaProduccion=tkinter.Label(self,text="TIEMPO FALLA PRODUCCION",font=fuente)
        self.labelPeriodoFallaProduccion.place(x=600,y=py) 
        self.Objetos[3].setLables(self.labelPeriodoFallaProduccion,self.label4)
        py=py+dy 

        tkinter.Label(self,text="AFILADO",font=fuente).place(x=10,y=py)
        self.label5=tkinter.Label(self,text="PULSA TECLA 5",font=fuente)
        self.label5.place(x=300,y=py)
        self.labelPeriodoAfilado=tkinter.Label(self,text="TIEMPO AFILADO",font=fuente)
        self.labelPeriodoAfilado.place(x=600,y=py) 
        self.Objetos[4].setLables(self.labelPeriodoAfilado,self.label5)
        py=py+dy 

        tkinter.Label(self,text="MTTO",font=fuente).place(x=10,y=py)
        self.label6=tkinter.Label(self,text="PULSA TECLA 6",font=fuente)
        self.label6.place(x=300,y=py)
        self.labelPeriodoMtto=tkinter.Label(self,text="TIEMPO MTTO",font=fuente)
        self.labelPeriodoMtto.place(x=600,y=py) 
        self.Objetos[5].setLables(self.labelPeriodoMtto,self.label6)
        py=py+dy 

        self.label6=tkinter.Label(self,text="AUTOMATICO",font=fuente)
        self.label6.place(x=10,y=py)
        self.labelTrabajado=tkinter.Label(self,text="TIEMPO TRABAJADO:",font=fuente)
        self.labelTrabajado.place(x=600,y=py)
        self.Objetos[6].setLables(self.labelTrabajado,self.label6)
        py=py+dy 

    #-------------------------------------------------------------Inicializa el teclado------------------------------------------------------------------------------------------------------------
    def Inicializateclado(self):
        escuchador = kb.Listener(self.onKeyPress)
        escuchador.start()
    #---------------------------------------------------------Detecta la tecla pulsada-------------------------------------------------------------------------------------------------------------
    def onKeyPress(self,tecla):
        try:  
            self.teclaPresionada(tecla.char)  
        except Exception as err:
            print(f"ocurrio un error {err=}, {type(err)=}")  
    #-------------------------------------------------------------procesa la tecla---------------------------------------------------------------------------------------------------------------  
    def teclaPresionada(self,tecla):
        try:  
            #recorro los objetos para pasarles la tecla que se presiono
            for objeto in self.Objetos:
                if objeto.keyPress(tecla)==True:
                    #hay que guardar los datos
                    self.guardaTiempo()
                    self.limpiaDatos(objeto) #mando a limpiar todos los contadores menos el procesado
                    return 
        except Exception as err:
            print(f"ocurrio un error en EvntanaPrincipal:teclaPresionada {err=}, {type(err)=}")    
    #-----------------------------------------------------------se llama cuando se activa la maquina-----------------------------------------------
    def guardaTiempo(self):
        #en este caso se simula que se detecto el funcionamiento del pin12 y se guarda el valor enel archivo
        time.sleep(.1)
        datos=[]
        ok=False
        for objeto in self.Objetos:
            valor=objeto.DameTiempo()
            datos.append(valor)    
            if(valor!=""):
                ok=True
        if(ok==True):
            archivo=XArchivo()
            archivo.EscribeArchivo(datos)
            self.limpiaDatos(None)

    #-----------------------Limpia los datos-------------------------------------------------------------------------------------
    def limpiaDatos(self, objeto):
        for objeto1 in self.Objetos:
            if objeto!=None and objeto1.Texto!=objeto.Texto:
                objeto1.desactiva()
    #----------------------------------------------------------funcion que se ejecuta cada segundo---------------------------------------------------
    def timer1(self):        
        try:
            #le aviso a los objetos que ha pasado un segundo
            for objeto in self.Objetos:
                objeto.tick()
            #mando a mostrar los tiempo
            #reviso el estado de la maquina
            if self.gpio.maquinaStatus()==1:
                if self.activo==False:
                    #marco que ya esta trabajando
                    self.teclaPresionada('p')
                    self.activo=True
            else:
                #la maquina esta detenid
                if self.activo==True:
                    #se acaba de detener
                    self.guardaTiempo()
                    self.Objetos[6].desactiva()
                    self.labelTrabajado.config(text="Detenida")
                    self.label6.config(fg="red")
            self.after(1000,self.timer1)
        except Exception as err:        
            print(f"ocurrio un error en VentanaPrincipal:timer1 {err=}, {type(err)=}")    
            self.after(1000,self.timer1)
    