def sumarllista(a):
	sumatori = 0
	for i in a:
		sumatori +=1
	return sumatori


def Llistat_multiplicat(llista):

	# Multiplicar un per un
	resultat = 1
	for x in llista:
		resultat *= x
	return resultat

x = [1,2,3,4,5,6]
print("El sumatori és: ",sumarllista(x))
print("El multiplicat és: ",Llistat_multiplicat(x))
