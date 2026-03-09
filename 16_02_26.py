#panel windows
import os #es importar os("os" es una librería estándar incorporada que permite interactuar con el sistema operativo subyacente)
import time
def esperar(texto): #es opcional esta definicion de funcion, muetra el porcentje de carga
    for x in range(5):
        os.system("cls")
        print(f"cargando {texto} {x*20} %")
        time.sleep(0.5) #time.sleep(segundos): Suspende la ejecución del hilo actual durante el número de segundos especificado.

while True:
    os.system("cls")
    print("dashboard de windows")
    op= int(input("1.Calc\n2.paint\n3.apagar\n4.no apagar\n0.salir\nopcion:"))
    if op==1:
        esperar("calculadora") #llama a la funcion definida esperar(texto)  
        os.system("calc") #calc es el comando en la pc de calculadora, se utiliza para poder llamar a la aplicacion desde python 
    
    elif op==2:
        esperar("Paint")
        os.system("mspaint") #debemos sber como se llama paint para poder importar, el comando
    
    elif op==3:
        esperar("apagando en 5 min")
        os.system("shutdown -s -t 300") 

    elif op==4:
        esperar("cancelar apagado")
        os.system("shutdown -a") 
    
    elif op==0:
        print("FIN")
        break

    else:
        print("(0_0)")