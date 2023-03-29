import random
import time

puntuacion = 0  # Variable para almacenar la puntuación

# Función donde explicamos qué pasa
def intro():
    print("""En una época donde los gigantes gobiernan Menorca. Nosotros necesitamos comer.
    Estamos siguiendo el rastro del olor del alimento, pero nos encontramos en una encrucijada.
    Al final de cada camino hay un talayot, en uno viven los gigantes buenos que nos invitarán,
    y en el otro son unos caníbales hambrientos que nos comerán apenas nos vean.
    """)

# Función donde preguntamos a qué talayot queremos ir
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("¿A qué talayot quieres ir? Introduce 1 o 2: ")
    return talaiot

# Función que nos indica si compartirán la comida o si seremos nosotros su comida
def trobada(talaiot):
    global puntuacion  # Para acceder a la variable puntuación

    print("Te estás acercando al talayot...")
    time.sleep(2)
    print("Está oscuro y es tenebroso...")
    time.sleep(2)
    print("Un gran gigante salta delante de ti, te coge y...")
    print("")
    time.sleep(2)
    gegantamic = random.randint(1, 2)
    if talaiot == str(gegantamic):
        print("¡Te invita a comer!")
        puntuacion += 1  # Sumamos 1 punto a la puntuación
    else:
        print("¡Te come de un bocado...ÑAMÑAMÑAM!")
        puntuacion -= 1  # Restamos 1 punto a la puntuación

# Función principal
partidaNova = "si"
while puntuacion<0 == exit and partidaNova == "s" or partidaNova == "si":
    intro()
    nTalaiot = canviTalaiot()
    trobada(nTalaiot)
    print("Tu puntuación actual es:", puntuacion)
    partidaNova = input("¿Quieres volver a jugar? Introduce si o no: ")
    print("\n")