#--------------------------------------------------------clase que se encarga de controlar el tiempo de los rubros----------------------------------------------------------------
class Objeto:
    def __init__(self,texto,tecla) -> None:
        self.Texto=texto
        self.Tiempo=0 #el tiempo se almacena en segundos
        self.Activo=False #cuando este activo, se va a contar el tiempo
        self.Tecla=tecla 
    #---------------------------------------------------funcion que se llama cada segundo para llevar el conteo-------------------------------------------------------------------
    def tick(self):
        if self.Activo==True:
            self.Tiempo+=1 #se incrementa un segundo
            #actualizo el label
            self.LabelText.config(text=self.Texto+self.DameTiempo())
    #--------------------------funcion que se llama cada que se presiona una tecla y se activa si la tecla es la especificada y regresa true si se proceso la tecla-----------------
    def keyPress(self, tecla):
        if self.Tecla==tecla:
            self.Activo=True
            #marco el label del color
            self.LabelTecla.config(fg="green")
            return True
        return False 
    #---------------------------------------------------funcion desactiva el conteo y lo reinicia a cero------------------------------------------------------------------------------
    def desactiva(self):
        self.Activo=False
        self.Tiempo=0
         #actualizo el label
        self.LabelText.config(text=self.Texto+self.DameTiempo())
        #desactivo el color
        self.LabelTecla.config(fg="black")
    #-------------------------------------------------funcion que regresa el tiempo que ha permanecido activo en una cadena-----------------------------------------------------------
    def DameTiempo(self):
        if self.Tiempo==0:
            return ""
        horas=0
        minutos=0
        segundos=self.Tiempo
        if(segundos>3600):
            horas=int(segundos/3600)
            segundos=segundos-(horas*3600)
        if segundos>60:
            minutos=int(segundos/60)
            segundos=segundos-(minutos*60)
        return str(horas)+":"+str(minutos)+":"+str(segundos)
    #-------------------------------------------------funcion que asigna los labels para actualizar la interface grafica-------------------------------------------------------------------
    def setLables(self,labelText,labelTecla):
        self.LabelText=labelText
        self.LabelTecla=labelTecla

