def sumarllista(a):
	sumatori = 0
	for i in a:
		sumatori = sumatori + (i*i) #sumatori +=(i*i)
	return sumatori

# Funció de multiplicar
def Llistat_multiplicat(llista):

	# Multiplicar un per un
	resultat = 1
	for x in llista:
		resultat *= x
	return resultat

x = [1,7,1,7,1]
print("El sumatori és: ",sumarllista(x))
print("El multiplicat és: ",Llistat_multiplicat(x))