x = input("Introdueixi la primera paraula: ")
y = input("Introdueixi la segona paraula: ")

if x[-3:] == y[-3:]:
    print("Les paraules {} i {} rimen les darreres tres lletres {}".format(x, y, x[-3:]))
elif x[-2:] == y[-2:]:
    print("Les paraules {} i {} rimen les darreres dues lletres {}".format(x, y, x[-2:]))
elif x[-1:] == y[-1:]:
    print("Les paraules {} i {} rimen la darrera lletra {}".format(x, y, x[-1:]))
else:
    print("Les paraules {} i {} no rimen".format(x, y))

