# Donat un caràcter que ens torni true si és una vocal i fals si no ho és
def vocal(a):

    if (a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U'):
        return True
    else:
        return False
    
# Programa principal

a = input("Escriu un caràcter: ")
print("Si posa *True* és una vocal si posa *False* és una consonant: ",vocal(a))