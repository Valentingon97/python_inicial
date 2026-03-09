#importacion de funciones
from tkinter import *
from tkinter import ttk

#definicion de funcion
def saludar():
    print("saldo actual: 2000") #en esta parte al ejecutar va a mostrar en la terminal y no en la ventana emergente, por eso es que es mejor un return

#creacion de la ventana
ventana= Tk()
ventana.title("LOGIN")
ventana.geometry("400x200") #el tamaño de la ventana emergente
frm= ttk.Frame(ventana, padding=10)
frm.grid()
ttk.Label(frm, text="descubre el texto").grid(column=0, row=0)
ttk.Button(frm, text="saldo", command= saludar).grid(column=1, row=0)
#mensaje= ttk.Label(frm, text="-------").grid(column=0, row=1)

#refresca la ventana
ventana.mainloop()

