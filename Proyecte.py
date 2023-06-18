import pygame
import random

# Dimensiones de la ventana del juego
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMANIO_BLOQUE = 30
ANCHO_TABLERO = 10
ALTO_TABLERO = 20
MARGEN_SUPERIOR = 50
COLOR_FONDO = (0, 0, 0)
COLOR_BLOQUE = (255, 255, 255)

# Definición de las piezas y sus formas
FORMAS_PIEZAS = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]


def crear_tablero():
    """Crea una matriz vacía para el tablero del juego."""
    tablero = [[0] * ANCHO_TABLERO for _ in range(ALTO_TABLERO)]
    return tablero


def dibujar_bloque(surface, x, y):
    """Dibuja un bloque en la posición especificada."""
    pygame.draw.rect(surface, COLOR_BLOQUE, (x, y, TAMANIO_BLOQUE, TAMANIO_BLOQUE))


def dibujar_tablero(surface, tablero):
    """Dibuja el tablero del juego."""
    for fila in range(ALTO_TABLERO):
        for columna in range(ANCHO_TABLERO):
            if tablero[fila][columna] == 1:
                x = columna * TAMANIO_BLOQUE
                y = fila * TAMANIO_BLOQUE + MARGEN_SUPERIOR
                dibujar_bloque(surface, x, y)


def colisiona_pared(pieza, posicion_x):
    """Verifica si la pieza colisiona con una pared."""
    for fila in range(len(pieza)):
        for columna in range(len(pieza[0])):
            if pieza[fila][columna] and (posicion_x + columna < 0 or posicion_x + columna >= ANCHO_TABLERO):
                return True
    return False


def colisiona_suelo(pieza, posicion_x, posicion_y, tablero):
    """Verifica si la pieza colisiona con el suelo o con otras piezas."""
    for fila in range(len(pieza)):
        for columna in range(len(pieza[0])):
            if pieza[fila][columna]:
                if (posicion_y + fila >= ALTO_TABLERO or
                        tablero[posicion_y + fila][posicion_x + columna]):
                    return True
    return False


def rotar_pieza(pieza):
    """Rota la pieza 90 grados en sentido antihorario."""
    nueva_pieza = [[0] * len(pieza) for _ in range(len(pieza[0]))]
    for fila in range(len(pieza)):
        for columna in range(len(pieza[0])):
            nueva_pieza[columna][len(pieza) - fila - 1] = pieza[fila][columna]
    return nueva_pieza


def eliminar_filas_completas(tablero):
    """Elimina las filas completas del tablero y desplaza las superiores hacia abajo."""
    filas_completas = []
    for fila in range(ALTO_TABLERO):
        if all(tablero[fila]):
            filas_completas.append(fila)
    for fila in filas_completas:
        del tablero[fila]
        tablero.insert(0, [0] * ANCHO_TABLERO)


def obtener_pieza_aleatoria():
    """Selecciona aleatoriamente una de las formas de pieza."""
    return random.choice(FORMAS_PIEZAS)


def joc():
    """Implementación del juego Tetris."""
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Tetris")

    reloj = pygame.time.Clock()
    tablero = crear_tablero()
    pieza_actual = obtener_pieza_aleatoria()
    posicion_x = ANCHO_TABLERO // 2 - len(pieza_actual[0]) // 2
    posicion_y = 0
    puntuacion = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not colisiona_pared(pieza_actual, posicion_x - 1):
                        posicion_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if not colisiona_pared(pieza_actual, posicion_x + 1):
                        posicion_x += 1
                elif event.key == pygame.K_DOWN:
                    if not colisiona_suelo(pieza_actual, posicion_x, posicion_y + 1, tablero):
                        posicion_y += 1
                elif event.key == pygame.K_UP:
                    pieza_actual = rotar_pieza(pieza_actual)

        if not colisiona_suelo(pieza_actual, posicion_x, posicion_y + 1, tablero):
            posicion_y += 1
        else:
            for fila in range(len(pieza_actual)):
                for columna in range(len(pieza_actual[0])):
                    if pieza_actual[fila][columna]:
                        tablero[posicion_y + fila][posicion_x + columna] = 1
            eliminar_filas_completas(tablero)
            pieza_actual = obtener_pieza_aleatoria()
            posicion_x = ANCHO_TABLERO // 2 - len(pieza_actual[0]) // 2
            posicion_y = 0

            if colisiona_suelo(pieza_actual, posicion_x, posicion_y, tablero):
                pygame.quit()
                sys.exit()

        ventana.fill(COLOR_FONDO)
        dibujar_tablero(ventana, tablero)
        for fila in range(len(pieza_actual)):
            for columna in range(len(pieza_actual[0])):
                if pieza_actual[fila][columna]:
                    x = (posicion_x + columna) * TAMANIO_BLOQUE
                    y = (posicion_y + fila) * TAMANIO_BLOQUE + MARGEN_SUPERIOR
                    dibujar_bloque(ventana, x, y)
        pygame.display.update()
        reloj.tick(5)

# Programa principal
def programa_principal():
    opcio = input("Selecciona una de les 4 aplicacions (1-4): ")
    if opcio == "1":
        print("Has seleccionat la primera funció.")
        # Lògica de la primera funció (treballar amb llistes, números aleatoris)
    elif opcio == "2":
        print("Has seleccionat la segona funció.")
        # Lògica de la segona funció (treballar amb fitxers i guardar informació)
    elif opcio == "3":
        print("Has seleccionat la tercera funció (joc).")
        joc()  # Lògica de la tercera funció (implementació del joc Tetris)
    elif opcio == "4":
        print("Has seleccionat la quarta funció.")
        # Lògica de la quarta funció (treballar amb objectes, classe, herència, polimorfisme)
    else:
        print("Opció no vàlida. Si us plau, selecciona una opció entre 1 i 4.")


if __name__ == "__main__":
    programa_principal()