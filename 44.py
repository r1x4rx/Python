def eliminarcapicua(lista):
    if lista == []:
        return []
    elif len(lista) == 1:
        return []
    elif len(lista) == 2:
        return []
    elif lista[0] == lista[-1]:
        return eliminarcapicua(lista[1:-1])
    else:
        return [lista[0]] + eliminarcapicua(lista[1:-1]) + [lista[-1]]
