def comptar_vocals(paraula):
    # Inicialitzem un diccionari per comptar les vocals
    vocals = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Recorrem la paraula i actualitzem el comptador de cada vocal
    for lletra in paraula:
        if lletra.lower() in vocals:
            vocals[lletra.lower()] += 1
    
    # Retornem el diccionari de comptadors
    return vocals

# Exemple d'ús de la funció
paraula = "Ratapinyada"
comptadors = comptar_vocals(paraula)
print(f"A la paraula '{paraula}' hi ha {comptadors['a']} a's, {comptadors['e']} e's, {comptadors['i']} i's, {comptadors['o']} o's i {comptadors['u']} u's.")

