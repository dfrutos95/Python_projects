#Buscaminas
#*****************************************************************************************************
#
#*****************************************************************************************************
#IMPORTACIONES
import tkinter as tk 
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import Tk,Text,Button,END,re
import random


#CLASE PRINCIPAL
class Application(ttk.Frame):               #clase principal: la Aplicación
    minas=[]
    def __init__(self, formulario2):        #función de inicialización del formulario
        super().__init__(formulario2)
        self.formulario2 = formulario2;
        formulario2.title("Buscaminas")     #título del formulario
        #
        #Lista de botones 
        self.boton=[];
        aleatorios=[]
        c=0
        f=(-1)
        for i in range(100):
            self.boton.insert(i, self.crearBoton("", i))
            if i%10 ==0:
                c=0
                f=f+1
            self.boton[i].place(x=(c*60)+1, y=(f*60)+5, width=55, height=55)
            c=c+1
        #Repartimos minas
        def colocarMinas():
            j=0
            for x in range(10):
                while j<11:
                    n=random.randint(0, 99)
                    if n not in aleatorios:
                        
                        self.boton[random.choice(range(100))].config(text="m")
                        aleatorios.append(n)
                        j=j+1
        colocarMinas()


        return
    
    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, texto, id):
        return Button(self.formulario2, text=texto,font=("Helvetica",20), command=lambda:self.click(id), background='grey', foreground='grey')

    #Evento disparado al hacer click botones
    def click(self, id):
        boton=self.boton[id]
        if boton.cget('text') == "m":
            boton.configure(text="X")
            for i in range(100):
                self.boton[i].configure(text="X", disabledforeground="red", state="disabled")
        else:
            total=0
            if id>0 and id<9:
                if (self.boton[id-1].cget('text')=="m"):
                    total=total+1
                if (self.boton[id+1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+9].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+11].cget('text')=="m"):
                    total=total+1
            elif id%10==0 and id!=90:
                if (self.boton[id+1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+11].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-9].cget('text')=="m"):
                    total=total+1
            elif id>90 and id<99:
                if (self.boton[id-1].cget('text')=="m"):
                    total=total+1
                if (self.boton[id+1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-11].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-9].cget('text')=="m"):
                    total=total+1
            elif (id+1)%10==0 and id!=99 and id!=9:
                if(self.boton[id-1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-11].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+9].cget('text')=="m"):
                    total=total+1
            elif id==0:
                if(self.boton[id+1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+11].cget('text')=="m"):
                    total=total+1
            elif id==9:
                if(self.boton[id-1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+9].cget('text')=="m"):
                    total=total+1
            elif id==90:
                if(self.boton[id+1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-9].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-10].cget('text')=="m"):
                    total=total+1
            elif id==99:
                if(self.boton[id-1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-11].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-10].cget('text')=="m"):
                    total=total+1
            else:
                if (self.boton[id-1].cget('text')=="m"):
                    total=total+1
                if (self.boton[id+1].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-10].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-11].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+11].cget('text')=="m"):
                    total=total+1
                if(self.boton[id+9].cget('text')=="m"):
                    total=total+1
                if(self.boton[id-9].cget('text')=="m"):
                    total=total+1
            if total==0:
                boton.configure(text="", foreground='white', background="#00de1a")
            elif total==1:
                boton.configure(text=str(total), foreground='white', background="#fcba03")
            else:
                boton.configure(text=str(total), foreground='white', background="#de3800")
        return

#
# Configuración y lanzamiento #
#
formulario2=Tk()
formulario2.geometry("600x600+333+99")
app=Application(formulario2)
app.mainloop()