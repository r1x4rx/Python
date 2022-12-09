#Definir una funciosupersposicio() que agafi dues llistes i retorni vertader si hi ha
def superposicio(a, b):
    n = 0 #indica quants elements hi ha en comu
    for e in a:
        n += b.count(e)
    if n>0:
        return [n, True]
    else:
        return [0, False]

#Programa principal
a = input("Introdueix la primera llista d'elements com un string, sense espais: ")
b = input("Introdueix la segona llista d'elements com un string, sense espais: ")
c,d = superposicio(a,b)
if (c==0):
    print("Les dues llsites no tenen cap element en comu.")
else:
    print("Les llistes tenen ", c, " elements en comu")