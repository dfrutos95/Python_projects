import tkinter as tk        #librería a importar
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import Tk,Text,Button,END,re
from tkinter import *
import math
#CLASE PRINCIPAL
class Application(ttk.Frame):               #clase principal: la Aplicación
     
    def __init__(self, formulario2):        #función de inicialización del formulario
        
        super().__init__(formulario2)
        self.formulario2 = formulario2;
        formulario2.title("CALCULADORA")     #título del formulario
        #
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("ventana.TFrame",background="#282829")
        self.config(style="ventana.TFrame")
        self.operacion=""
        self.display=Text(formulario2, state="disabled", background="gray", foreground="white", font=("Helvetica", 60))
        self.display.place(x=6, y=3, width=wF-12, height=100)
       
        boton7=self.crearBoton(7);          boton8=self.crearBoton(8)
        boton9=self.crearBoton(9);          botonBorrar=self.crearBoton(u"\u232B",escribir=False)
        boton4=self.crearBoton(4);          boton5=self.crearBoton(5)
        boton6=self.crearBoton(6);          botonDividir=self.crearBoton("/")
        boton1=self.crearBoton(1);          boton2=self.crearBoton(2)
        boton3=self.crearBoton(3);          botonMulti=self.crearBoton("*")
        botonPunto=self.crearBoton(".");    boton0=self.crearBoton(0)
        botonSumar=self.crearBoton("+");    botonRestar=self.crearBoton("-")
        botonAC=self.crearBoton("AC", escribir=False)
        botonIgual=self.crearBoton("=", escribir=False)
        botonInvertir=self.crearBoton("+/-", escribir=False)
        botonRaiz=self.crearBoton("√", escribir=False)
        botonAC.configure(fg='black')
        botonBorrar.configure(fg='black')
        
        #Ubicar los botones 
        botones=[botonAC, botonInvertir, botonRaiz, botonBorrar, boton7, boton8, boton9, botonMulti, boton4, boton5, boton6, botonDividir,  boton1, boton2, boton3, botonRestar, botonPunto, boton0, botonIgual, botonSumar]
        i=0
        for f in range(0,5):
            for c in range(4):
                botones[i].place(x=(ww*c)+6, y=(hh*f)+hDisplay, width=w, height=h)
                i+=1
       # botonIgual.place(x=6, y=(hh*(f+1))+hDisplay, width=wF-12, height=h)
        #
        return
        

    #Crea un botón mostrando el valor pasado por parámetro
    def crearBoton(self, texto, escribir=True, ancho=4, alto=1):
        #en mi ordenador tengo que usar hightlightbackgrounf para que cambie el color del boton, en windows solo se usa background
        return Button(self.formulario2, text=texto, width=ancho, height=alto, font=("Helvetica",20), highlightbackground="#49494a", command=lambda:self.click(texto,escribir))
    def click(self, texto, escribir):
        if escribir:                        #<--- texto se ve en pantalla
            self.operacion+=str(texto)
            self.mostrar(texto)
        elif texto=="=" and self.operacion!="":
            resultado=str(eval(self.operacion)); self.operacion="";
            self.limpiarDisplay()
            self.mostrar(resultado)
            self.operacion+=str(resultado)  #<--- acumular para la operación siguiente
        elif texto==u"\u232B":              #<--- limpiar la pantalla
            resultado=str(self.operacion[:-1])
            self.limpiarDisplay()
            self.mostrar(resultado)
            self.operacion=resultado
        elif texto=="AC":
            self.operacion=""
            self.limpiarDisplay()
        elif texto=="+/-":
            resultado=int(self.operacion)*-1
            self.limpiarDisplay()
            self.mostrar(resultado)
            self.operacion=str(resultado)
        elif texto=="√":
            resultado=math.sqrt(int(self.operacion))
            self.limpiarDisplay()
            self.mostrar(resultado)
            self.operacion=str(resultado)
        return

    #Borrar display
    def limpiarDisplay(self):
        self.display.configure(state="normal")
        self.display.delete("1.0", END)
        self.display.configure(state="disabled")
        return

    def mostrar(self, valor):
        self.display.configure(state="normal")
        self.display.insert(END, valor)
        self.display.configure(state="disabled")
        return


# Configuración y lanzamiento #
hDisplay= 110;
hhh=200
wF=350; hF=700; ww=(wF/4)-2; w=ww-6; hh=hF/10; h=hh-6
f=5; x1=(ww*1)-w ; y1=(hh*f)+hhh; x2= (ww*2)-w; y2=(hh*f)+hhh; x3=(ww*3)-w; y3=(hh*f)+hhh; xres=(ww*4)-w; ysum=(hh*f)+hhh;
f=4; x4=(ww*1)-w ; y4=(hh*f)+hhh; x5= (ww*2)-w; y5=(hh*f)+hhh; x6=(ww*3)-w; y6=(hh*f)+hhh; xmul=(ww*4)-w; ymul=(hh*f)+hhh;
f=3; x7=(ww*1)-w ; y7=(hh*f)+hhh; x8= (ww*2)-w; y8=(hh*f)+hhh; x9=(ww*3)-w; y9=(hh*f)+hhh; xsum=(ww*4)-w; yres=(hh*f)+hhh;
#
formulario2=Tk()
formulario2.geometry(str(wF)+"x460+333+99")
app=Application(formulario2)
app.mainloop()