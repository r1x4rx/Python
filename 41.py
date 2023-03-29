numero = int(input("Introdueixi un número entre 1 i 20: "))

# Comprova que el número està dins del rang permès
if numero < 1 or numero > 20:
    print("El número ha d'estar entre 1 i 20.")
else:
    for i in range(1, 11):
        resultat = numero * i
        print(numero, "x", i, "=", resultat)