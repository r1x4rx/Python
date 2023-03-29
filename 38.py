x = int(input("Introdueixi un número natural (<100): "))
suma = 0
for i in range(1, x, 4):
    suma = suma + (i**2)
print("La suma dels quadrats de 4 posicions menys de {} és {} ".format(x, suma))