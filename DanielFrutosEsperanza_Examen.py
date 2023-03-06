#Examen pyhton 2 Daniel Frutos Esperanza
import tkinter as tk 
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import Tk,Text,Button,END,re
import random

class Application(ttk.Frame):              
    def __init__(self, formulario2):        
        super().__init__(formulario2)
        self.formulario2 = formulario2;
        formulario2.title("Daniel Frutos Examen")
        self.botonesPulsados=[]

        self.boton=[];
        c=0
        f=(-1)
        #Creamos la cuadricula
        for i in range(16):
            self.boton.insert(i, self.crearBoton("", i))
            if i%4 ==0:
                c=0
                f=f+1
            self.boton[i].place(x=(c*60)+1, y=(f*60)+5, width=55, height=55)
            if i == 3 or i == 7 or i==11 or i==12 or i ==13 or i==14 or i==15:
                self.boton[i].config(text=0, state="disabled", disabledforeground='black')
            c=c+1
        self.boton.insert(16, self.crearBoton("Nuevo tablero", 16))
        self.boton[16].place(x=1, y=241, width=239, height=55)
        self.boton[16].configure(command=lambda:self.nuevoTablero())
        #Asignamos numeros aleatorios a las casillas para sumarlos
        def asignarNumeros():
            for x in range(12):
                n=random.randint(1, 99)
                if x!=3 and x!= 7 and x!= 11:
                    self.boton[x].config(text=n)
                self.botonesPulsados.append(False)                
        asignarNumeros()
        def sumarRango(i, j, k):
            return int(self.boton[i].cget('text'))+int(self.boton[j].cget('text'))+int(self.boton[k].cget('text'))
        self.boton[3].config(text=sumarRango(0,1,2))
        self.boton[7].config(text=sumarRango(4,5,6))
        self.boton[11].config(text=sumarRango(8, 9, 10))
        self.boton[12].config(text=sumarRango(0, 4, 8))
        self.boton[13].config(text=sumarRango(1, 5, 9))
        self.boton[14].config(text=sumarRango(2, 6, 10))
        self.boton[15].config(text=int(sumarRango(3, 7, 11)))

        return
    
    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, texto, id):
        return Button(self.formulario2, text=texto,font=("Helvetica",20), command=lambda:self.click(id), background='grey', foreground='white')

    #Evento disparado al hacer click botones
    def nuevoTablero(self):
        self.botonesPulsados.clear()
        for x in range(12):
                n=random.randint(0, 99)
                if x!=3 and x!= 7 and x!= 11:
                    self.boton[x].config(text=n, background='grey')
                self.botonesPulsados.append(False) 
        def sumarRango(i, j, k):
            return int(self.boton[i].cget('text'))+int(self.boton[j].cget('text'))+int(self.boton[k].cget('text'))
        self.boton[3].config(text=sumarRango(0,1,2))
        self.boton[7].config(text=sumarRango(4,5,6))
        self.boton[11].config(text=sumarRango(8, 9, 10))
        self.boton[12].config(text=sumarRango(0, 4, 8))
        self.boton[13].config(text=sumarRango(1, 5, 9))
        self.boton[14].config(text=sumarRango(2, 6, 10))
        self.boton[15].config(text=int(sumarRango(3, 7, 11)))
    def click(self, id):
        boton=self.boton[id]
        if id >= 0 and id <3:
            respuesta=self.boton[3]
            if id == 0:
                respuesta2=self.boton[12]
            elif id == 1:
                respuesta2=self.boton[13]
            elif id == 2:
                respuesta2=self.boton[14]
        elif id >3 and id <=6:
            respuesta=self.boton[7]
            if id == 4:
                respuesta2=self.boton[12]
            elif id == 5:
                respuesta2=self.boton[13]
            elif id == 6:
                respuesta2=self.boton[14]
        elif id >7 and id<=10:
            respuesta=self.boton[11]
            if id == 8:
                respuesta2=self.boton[12]
            elif id == 9:
                respuesta2=self.boton[13]
            elif id == 10:
                respuesta2=self.boton[14]
        if self.botonesPulsados[id]:
            totalSuma=int(respuesta.cget('text'))+int(self.boton[id].cget('text'))
            respuesta.configure(text=totalSuma)
            respuesta2.configure(text=int(respuesta2.cget('text')+int(self.boton[id].cget('text'))))
            self.botonesPulsados[id]=False
            boton.configure(background='grey')  #Al des-pulsar el boton lo ponemos gris de vuelta  para señalizarlo
        else:
            totalSuma = int(respuesta.cget('text')-int(self.boton[id].cget('text')))
            respuesta.configure(text=totalSuma)
            respuesta2.configure(text=(int(respuesta2.cget('text')-int(self.boton[id].cget('text')))))
            self.botonesPulsados[id]=True
            boton.configure(background='blue')  #Al pulsar el boton lo ponemos azul para marcalo
        self.boton[15].configure(text=int(self.boton[3].cget('text'))+int(self.boton[7].cget('text'))+int(self.boton[11].cget('text')))
            
        return

#
# Configuración y lanzamiento #
#
formulario2=Tk()
formulario2.geometry("240x295+333+99")
app=Application(formulario2)
app.mainloop()