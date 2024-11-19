salari = 58462

iva = 0
if salari < 15000:
    iva = 0
elif salari > 15000 and salari < 30000:
    iva = 10
elif salari > 30000 and salari < 60000:
    iva = 21
else:
    print("Inserta un salari menor")

if salari < 60000:
    ivaFinal = salari * iva / 100
    print(f"El iva aplicat a un salari de {salari} es de {ivaFinal}")