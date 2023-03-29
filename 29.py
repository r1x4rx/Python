def noms_que_comencen_per(llista_noms):
    comptador = 0
    for nom in llista_noms:
        if nom[0] == 'a':
            comptador += 1
    return comptador
noms = ['Anna', 'Maria', 'Albert', 'Arnau', 'Xavier', 'Adriana']
noms_comencen_per_a = noms_que_comencen_per(noms)
print("Hi ha", noms_comencen_per_a, "noms que comencen per la lletra 'a'.")