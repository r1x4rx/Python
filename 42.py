numero = int(input("Introdueixi un número: "))
suma = 0

# Sumem els dígits del número
while numero > 0:
    digit = numero % 10
    suma += digit
    numero //= 10

# Determinem si la suma és parella o senar
if suma % 2 == 0:
    print("La suma dels dígits és parella.")
else:
    print("La suma dels dígits és senar.")
