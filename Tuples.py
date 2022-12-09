a=[1,2,3]

b = tuple (a)

for e in b :
    print(e)

for i in range(len(b)):
    print(i)

for i,e in enumerate(b):
    print("Posició:",i,"Valor",e)

x,y,z = b
print("X=",x,"Y=",y,"Z=",z)