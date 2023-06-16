import random
import os
import sys

try:
    import webbrowser
except ImportError:
    webbrowser = None

# importar altres llibreries segons necessitat

def menu():
    print("Benvingut al programa!")
    print("1. Trabajar con listas y números aleatorios")
    print("2. Trabajar con Ficheros")
    print("3. Tetris")
    print("4. Trabajar con objetos, clases, herencia y polimorfismo")
    print("5. Trabajar con Big Data, scrapping, etc.")
    print("6. Montar un servicio web")
    print("0. Salir")

    opcio = int(input("Escoge una opcion: "))

    return opcio

def listas_aleatorias():
    # implementació de la funció
    llista = []
    for i in range(10):
        llista.append(random.randint(1, 100))

    print("Llista generada aleatòriament:", llista)

def trabajar_archivos():
    # implementació de la funció
    pass

def tetris():
    # implementació de la funció
    pass

def clases_objetos():
    # implementació de la funció
    pass

def big_data_scrapping():
    # implementació de la funció
    pass

def servicio_web():
    # implementació de la funció
    pass

def main():
    opcio = menu()

    while opcio != 0:
        if opcio == 1:
            listas_aleatorias()
        elif opcio == 2:
            trabajar_archivos()
        elif opcio == 3:
            tetris()
        elif opcio == 4:
            clases_objetos()
        elif opcio == 5:
            big_data_scrapping()
        elif opcio == 6:
            servicio_web()
        else:
            print("Opción incorrecta. Porfavor, vuelvelo a intentar.")

        opcio = menu()

    print("Gracias para utilizar el programa. Hasta luego!")
    
    
    Clases vehiculos
    
    class Vehicle:
    numvehicles = 0 
    def __init__(self, nom):
        self.nom = nom 
        self.velocitat = 0
        self._protected_var = 10
        self.__private_var = 20   
    def acceleració(self):
        self.velocitat += 1
    def renou_motor(self):
        pass
    def get_private_var(self):
        return self.__private_var
 
objecte = Vehicle("Coche") 
print(objecte._protected_var) 
print(objecte.get_private_var())
    
    
    
    
    
    
Polimorfisme


class Forma:
    def area(self): # Definim un mètode abstracte que s’ha de definir per les subclasses
        pass

class Rectangle(Forma):
    def __init__(self, width, height):
        self.width = width 
        self.height = height
    def area(self):
        return self.width * self.height  # Retornem l’àrea del rectangle

class Cercle(Forma):
    def __init__(self, radi):
        self.radius = radi 
    def area(self):
        return 3.14 * self.radi ** 2  # Retornem l’àrea del cercle

formes = [Rectangle(4, 5), Cercle(7)]  
for f in formes:
    print(f.area()) 











Tetris


import pygame
import random

# Inicializar pygame
pygame.init()

# Definir los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir las dimensiones de la pantalla
LARGO_PANTALLA = 600
ALTO_PANTALLA = 700

# Crear la pantalla
pantalla = pygame.display.set_mode((LARGO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Tetris")

# Definir las dimensiones de un bloque
LARGO_BLOQUE = 30
ALTO_BLOQUE = 30

# Definir la posición inicial del tablero
X_TABLERO = 100
Y_TABLERO = 50

# Definir la matriz del tablero
tablero = []
for fila in range(20):
    fila_tablero = []
    for columna in range(10):
        fila_tablero.append(0)
    tablero.append(fila_tablero)

# Definir las piezas
piezas = [
    [[1, 1, 1], [0, 1, 0]],
    [[2, 2], [2, 2]],
    [[3, 0], [3, 3], [0, 3]],
    [[0, 4], [4, 4], [4, 0]],
    [[5, 5, 0], [0, 5, 5]],
    [[6, 6, 6, 6]],
    [[7, 7], [7, 7]],
]

    
    
