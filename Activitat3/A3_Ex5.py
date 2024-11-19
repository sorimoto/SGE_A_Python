num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

parell = []
senar = []
sumaParells = 0
sumaSenars = 0

for i in num:
    if i % 2 == 0:
        parell += [i]
    else:
        senar += [i]
for i in parell:
    sumaParells += i
for i in senar:
    sumaSenars += i

print(f"Suma parells: {sumaParells}. Suma senars:{sumaSenars}")