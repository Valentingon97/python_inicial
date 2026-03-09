# Diccionario Español -> Inglés
diccionario = {
    "hola": "hello",
    "adios": "goodbye",
    "gracias": "thank you",
    "perro": "dog",
    "gato": "cat"
}

while True:
    palabra = input("\nIngrese una palabra en español (0 para salir): ").lower()
    
    # Condición para salir
    if palabra == "0":
        print("Programa finalizado.")
        break
    
    # Verificar si existe en el diccionario
    if palabra in diccionario:
        print("Traducción:", diccionario[palabra])
    else:
        print("La palabra no existe en el diccionario.")
        opcion = input("¿Desea agregarla? (s/n): ").lower()
        
        if opcion == "s":
            traduccion = input("Ingrese la traducción en inglés: ").lower()
            diccionario[palabra] = traduccion
            print("Palabra agregada correctamente.")
        else:
            print("Palabra no agregada.")

print("\nDiccionario final:")
for esp, ing in diccionario.items():
    print(esp, ":", ing)
    