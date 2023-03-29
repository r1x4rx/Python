numero = int(input("Introdueixi un número: "))

while numero > 0:
    digit = numero % 10
    if digit % 2 == 0:
        print(digit)
    numero //= 10