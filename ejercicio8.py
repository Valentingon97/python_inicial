#import os #opcional, es una libreria

agenda={"emergencia":"911", "bomberos": "120"}
def cargar_agenda():
    nombre= input("ingrse nombre: ")
    tel= input("ingrse telefono: ")
    agenda[nombre]= tel

def ver_agenda():
    print(agenda)
    
while True:
    print("agenda telefonica")
    opcion=int(input("1.cargar\n2.Ver\n0.Salir\nelige: ")) #variable global
    if(opcion==1):
        cargar_agenda()
        #os.system("cls") #parte de la libreria
    elif(opcion==2):
        #os.system("cls")
        ver_agenda()
    elif(opcion==0):
        break
    else:
        print("?")