num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

parell = []
senar = []

for i in num:
    if i % 2 == 0:
        parell += [i]
    else:
        senar += [i]

print(f"Números parells: {parell}. Números senars: {senar}")