import math

def es_primo(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqrt_num = int(math.sqrt(num)) + 1
    for i in range(3, sqrt_num, 2):
        if num % i == 0:
            return False
    return True

# PPrincipal
nnumersprimers = 0
b = []
for num in range(1, 101):
    if es_primo(num):
        b.append(num)
        nnumersprimers += 1
print("Hi ha {} números primers i són {}".format(nnumersprimers, b))
