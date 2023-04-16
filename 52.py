def parells():
    a = []
    for i in range(2, 101, 2):
        a.append(i)
    return a

def senars():
    a = []
    for i in range(1, 100, 2):
        a.append(i)
    return a

#PPrincipal
pares = parells()
print("Els parells d'1 a 100 són {}".format(pares))
senars = senars()
print("Els senars d'1 a 100 són {}".format(senars))
