def mostrar_majors_que(tupla, valor):
    for num in tupla:
        if num > valor:
            print(num)
# Demanar a l'usuari que introdueixi els valors enters de la tupla
tupla = tuple(map(int, input("Introdueix els valors enters de la tupla separats per espais: ").split()))

# Cridar a la funció mostrar_majors_que() amb el valor 18
mostrar_majors_que(tupla, 18)
