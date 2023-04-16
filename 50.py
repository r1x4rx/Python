def llegir_llista_paraules():
    b = []
    a = ""
    while a != ".":
        a = input("Introdueixi la següent paraula: ")
        if a != ".":
            b.append(a)
    b.append(".") # Agrega el punto final a la lista
    b.sort()
    return b

def index_paraula(llista, paraula):
    indices = [i for i, e in enumerate(llista) if e == paraula]
    return indices

# Principal
a = llegir_llista_paraules()
p = input("Introdueix la paraula a cercar el seu índex: ")
b = index_paraula(a, p)
if len(b) == 0:
    print("Dins la llista {} no hi ha l'element {}".format(a, p))
else:
    print("Dins la llista {} la paraula {} apareix {} vegades en les següents posicions {}".format(a, p, len(b), b))
