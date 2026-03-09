import pyttsx3

#inicializar el motor
motor= pyttsx3.init()
texto="hola mundo"
motor.say(texto)
motor.runAndWait()