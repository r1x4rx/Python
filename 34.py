import random

def comprovar_codis(secret, intent):
    # Comprovem els números encertats i els que coincideixen però no estan en la posició correcta
    encertats = 0
    coincideixen = 0
    for i in range(len(secret)):
        if secret[i] == intent[i]:
            encertats += 1
        elif intent[i] in secret:
            coincideixen += 1
    return encertats, coincideixen

# Generem el codi secret aleatoriament
secret = "".join([str(random.randint(0, 9)) for i in range(4)])
print("Benvingut al MasterMind!")
print("Introdueix un codi de 4 xifres o prem ENTER per sortir.")

# Juguem fins que l'usuari encerti el codi o premi ENTER
while True:
    intent = input("Codi: ")
    if intent == "":
        print("Fins la propera!")
        break
    elif not intent.isdigit() or len(intent) != 4:
        print("Has d'introduir un codi de 4 xifres.")
    else:
        encertats, coincideixen = comprovar_codis(secret, intent)
        print(f"Encertats: {encertats}")
        print(f"Coincideixen: {coincideixen}")
        if encertats == 4:
            print("Felicitats! Has encertat el codi!")
            break