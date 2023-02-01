def crear_repetits(a,b):
    c = b*int(a)
    return c

def crear_punts(a):
    for e in a:
        c=crear_repetits(int(e), '.')
        print(c)

# PP
a = input("Escriu un nombre: ")
crear_punts(a)