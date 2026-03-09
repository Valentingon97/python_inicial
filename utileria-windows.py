from tkinter import *
import os

def abrirCalculadora():
    os.system("calc")

def abrirVisual():
    os.system("ipconfig")

ventana=Tk()
ventana.title("utilerias de windows")
ventana.geometry("400x200")

bCalc= Button(text="Calculadora", command= abrirCalculadora)
bCalc.place(x=50, y=50) #la funcion place(),permite ubicar los botones en posiciones exactas mediante coordenadas
bVisual= Button(text="visual studio code", command=abrirVisual)
bVisual.place(x=50, y=80)
#agregar un voton mas

ventana.mainloop()