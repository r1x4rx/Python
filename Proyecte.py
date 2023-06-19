import nacl
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

def generar_lista_aleatoria(n):
    """Genera una lista de n elementos con números aleatorios."""
    lista = []
    for _ in range(n):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista

def primera_funcio():
    print("Has seleccionat la primera funció.")
    n = int(input("Introdueix el nombre d'elements de la llista: "))
    llista = generar_lista_aleatoria(n)
    print("Llista generada:", llista)

def gestionar_archivo():
    """Permite gestionar un archivo para guardar, actualizar y eliminar información."""
    archivo = input("Introduce el nombre del archivo: ")

    while True:
        print("\n1. Mostrar contenido del archivo")
        print("2. Agregar información al archivo")
        print("3. Eliminar el archivo")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                with open(archivo, "r") as f:
                    contenido = f.read()
                    print("Contenido del archivo:")
                    print(contenido)
            except FileNotFoundError:
                print("El archivo no existe.")
        elif opcion == "2":
            informacion = input("Introduce la información a agregar al archivo: ")
            with open(archivo, "a") as f:
                f.write(informacion + "\n")
            print("Información agregada correctamente.")
        elif opcion == "3":
            try:
                confirmacion = input("¿Estás seguro de que deseas eliminar el archivo? (S/N): ")
                if confirmacion.upper() == "S":
                    os.remove(archivo)
                    print("Archivo eliminado correctamente.")
            except FileNotFoundError:
                print("El archivo no existe.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def segunda_funcio():
    print("Has seleccionat la segona funció (gestionar archivos).")
    gestionar_archivo()

class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def mostrar_informacion(self):
        pass


class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def mostrar_informacion(self):
        print("Rectángulo de color", self.color)
        print("Base:", self.base)
        print("Altura:", self.altura)
        print("Área:", self.area())


class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def mostrar_informacion(self):
        print("Círculo de color", self.color)
        print("Radio:", self.radio)
        print("Área:", self.area())


def cuarta_funcio():
    print("Has seleccionat la quarta funció (treballar amb objectes, classe, herència, polimorfisme).")
    figura1 = Rectangulo("rojo", 5, 3)
    figura2 = Circulo("azul", 2.5)

    figura1.mostrar_informacion()
    print()
    figura2.mostrar_informacion()

# Programa principal
def programa_principal():
    opcio = input("Selecciona una de les 4 aplicacions (1-4): ")
    if opcio == "1":
        print("Has seleccionat la primera funció.")
        primera_funcio()
        # Lògica de la primera funció (treballar amb llistes, números aleatoris)
    elif opcio == "2":
        print("Has seleccionat la segona funció.")
        segunda_funcio()
        # Lògica de la segona funció (treballar amb fitxers i guardar informació)
    elif opcio == "3":
        print("Has seleccionat la tercera funció (joc).")
        joc()  # Lògica de la tercera funció (implementació del joc Tetris)
    elif opcio == "4":
        print("Has seleccionat la quarta funció.")
        cuarta_funcio()
        # Lògica de la quarta funció (treballar amb objectes, classe, herència, polimorfisme)
    else:
        print("Opció no vàlida. Si us plau, selecciona una opció entre 1 i 4.")


if __name__ == "__main__":
    programa_principal()