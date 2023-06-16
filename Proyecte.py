import random
import os
import sys

try:
    import webbrowser
except ImportError:
    webbrowser = None

def menu():
    print("Benvingut al programa!")
    print("1. Trabajar con listas y números aleatorios")
    print("2. Trabajar con Ficheros")
    print("3. Tetris")
    print("4. Trabajar con objetos, clases, herencia y polimorfismo")
    print("5. Trabajar con Big Data, scrapping, etc.")
    print("6. Montar un servicio web")
    print("0. Salir")

    opcio = int(input("Escoge una opción: "))
    return opcio

def listas_aleatorias():
    llista = []
    for i in range(10):
        llista.append(random.randint(1, 100))

    print("Lista generada aleatoriamente:", llista)

def trabajar_archivos():
    # implementación de la función
    pass

def tetris():
    import pygame
    import random

    # Resto de la lógica del juego de Tetris
    # ...

def clases_objetos():
    class Vehicle:
        numvehicles = 0

        def __init__(self, nom):
            self.nom = nom
            self.velocitat = 0
            self._protected_var = 10
            self.__private_var = 20

        def acceleració(self):
            # implementación de la función
            pass

opcion = menu()

while opcion != 0:
    if opcion == 1:
        listas_aleatorias()
    elif opcion == 2:
        trabajar_archivos()
    elif opcion == 3:
        tetris()
    elif opcion == 4:
        clases_objetos()
    elif opcion == 5:
        print("Trabajando con Big Data, scrapping, etc.")
    elif opcion == 6:
        print("Montando un servicio web")
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

    opcion = menu()

print("¡Hasta luego!")

