def esta_ordenada(nums):
    # Comprovem si la llista està ordenada de forma ascendent
    if nums == sorted(nums):
        return "està ordenada de forma ascendent"
    # Comprovem si la llista està ordenada de forma descendent
    elif nums == sorted(nums, reverse=True):
        return "està ordenada de forma descendent"
    # Si no està ordenada de cap forma, retornem que no està ordenada
    else:
        return "no està ordenada"