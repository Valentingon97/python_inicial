#practica con listas
lista= [] #variable global
def cargar_lista():
    v= input("ingrese un valor: ") #variable interna
    lista.append(v)
def imprimir_lista():
    print("elementos de la lista")
    print(lista)
while True:
    print("gestionar lista")
    opcion=int(input("1.cargar\n2.Imprimir\n0.Salir\nElige: ")) #variable global
    if(opcion==1):
        cargar_lista()
    elif(opcion==2):
        imprimir_lista()
    elif(opcion==0):
        print("ADIOS")
        break
    else:
        print("no entiendo esa orden")