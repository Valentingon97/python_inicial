import os, time, random
def lanzar_dados():
    return random.randrange(1,7) #randrange es una funcion para que de numeros aleatorios solo numeros entre 1 y 6, tomando el 1 y n-1=7-1=6

while True:
    op=int(input("elige un numero del dado: "))
    if op>=1 and op <=6:
        os.system("cls") #limpia pantalla, el historial en la terminal
        print("elegiste el ", op) #se puede llama de esta forma al entero
        print("lanzamos el dado")
        time.sleep(3) #para tener un tiempo de espera
        dado= lanzar_dados()
        print(f"ha caido el {dado}") # o de esta forma se le puede llamar al entero con {} sin olvidar la f
        if dado==op:
            print("buena suerte, haz ganado")
        else:
            print("haz perdido, vuelve a intentarlo")
    else:
        print("juego terminado")
        break