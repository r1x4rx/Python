def hi_ha_duplicats(llista):
    """
    Aquesta funció comprova si hi ha algun element duplicat a la llista donada.
    Retorna True si hi ha algun element duplicat, False si tots els elements són únics.
    """
    return len(llista) != len(set(llista))