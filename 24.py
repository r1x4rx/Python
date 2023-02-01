def filtrar_paraules(a, num):
    b = list()
    for e in a:
        if num < len(e):
            b.append(e)
    return b

x = ("hola", "Si", "Un senyor damunt un ruc", "filosof", "Xouman",)
a = input("indicar la longitud de les paraules que vols filtrar: ")
y = filtrar_paraules(x,int(a))
print("Les paraules de igual o mes tamany de ", a, " son: ", y)