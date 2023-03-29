import random

def llista_20_elements():
    llista = []
    while len(llista) < 20:
        num = random.randint(1, 100)
        if num not in llista:
            llista.append(num)
    return llista