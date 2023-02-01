# Definir una funció superposicio() que agafi dues llistes i retorni vertader si hi
def superposicio(a, b):
    n = 0 # Indica quants elements hi ha en comú
    for e in a:
        n += b.count(e)
    if n>0:
        return [n, True]
    else:
        return [0, False]
    
# Programa Principal
a = input("Introdueix la primera llista d'elements com un string, sense espais: ")
b = input("Introdueix la segona llista d'elements com un string, sense espais: ")
c,d = superposicio(a,b)
if (c==0):
    print("Les dues llistes no tenen cap element en comú.")
else:
    print("Les llistes tenen ", c, " element en comú")