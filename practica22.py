# Diccionario con usuarios y contraseñas
usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "admin": "admin2024"
}

# Solicitar usuario
usuario = input(f"Ingrese su usuario: ")

# Verificar si el usuario existe
if usuario in usuarios:
    intentos = 0
    acceso = False
    
    # Permitir solo 3 intentos
    while intentos < 3 and not acceso:
        contraseña = input("Ingrese su contraseña: ")
        
        if contraseña == usuarios[usuario]:
            print("✅ Acceso concedido")
            acceso = True
        else:
            intentos += 1
            print(f"❌ Contraseña incorrecta. Intento {intentos} de 3")
    
    if not acceso:
        print("🔒 Cuenta bloqueada por demasiados intentos fallidos")
else:
    print("⚠️ El usuario no existe")