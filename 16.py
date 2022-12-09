# Definim una funció
def Reves(a):
    # Indicam quina ha de ser la variable
    b = ''

    # Ordenam quin és el loop
    for x in a:
        # Aqui giram l'ordre
        b = x + b
    return b

a = 'Ramis'

# Aqui sortiràn els resultats
print('Text original: ', a)
print('Text canviat: ', Reves(a))