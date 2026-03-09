PI= 3.14

def menu():
    print("1.Calcular area del triangulo")
    print("2.Calcular perimetro del triangulo")
    print("3.calcular area del rectangulo")
    print("4.calcular perimetro del rectangulo")
    print("5.calcular area de la circunferencia")
    print("6.calcular perimetro de la circunferencia")
    print("7.salir")
    op= input("opcion: ")
    return op

def area_triangulo(base, altura):
    return(base*altura)/2

def perimetro_triangulo(lado1,lado2,lado3):
    return lado1+lado2+lado3

def area_rectangulo(largo,ancho):
    return largo * ancho

def perimetro_rectangulo(largo,ancho):
    return(largo + ancho) * 2

def area_elipse(radio, excentricidad=1):
    pass

def perimetro_elipse(radio):
    return 2*PI*radio

if __name__ == "__main__": #doble guion bajo
    while True:
        opcion= menu()
        if opcion=="1":
            base= float(input("base:"))
            altura= float(input("altura:"))
            resultado= area_triangulo(base, altura) #aqui es donde llama a la funcion definida
            print(f"el area es {resultado} u2")
        
        elif opcion=="2":
            l1=float(input("lado1:"))
            l2=float(input("lado2:"))
            l3=float(input("lado3:"))
            resultado=perimetro_triangulo(lado1,lado2,lado3)
            print(f"el perimetro es {resultado}u")
        
        elif opcion=="3":
            largo= float(input("largo:"))
            ancho=float(input("ancho:"))
            resultado= area_rectangulo(largo,ancho) 
            print(f"el area es {resultado}u2")
        
        elif opcion=="4":
            largo= float(input("largo:"))
            ancho=float(input("ancho:"))
            resultado= perimetro_rectangulo(largo,ancho)
            print(f"el perimetro es {resultado} u")
        
        elif opcion=="5":
            radio= float(input("radio:"))
            resultado= area_elipse(radio, excentricidad=1)
            print(f"el area es {resultado}u2")
        
        elif opcion=="6":
            radio= float(input("radio:"))
            resultado= perimetro_elipse(radio)
            print(f"el perimetro es {resultado} u")
        
        elif opcion=="7":
            break

        
        
        



    



    
    