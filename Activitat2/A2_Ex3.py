nota = 6.25

if nota < 5:
    print(f"L'alumne ha suspes amb un {nota}")
elif nota >= 5 and nota <= 6.5:
    print(f"L'alumne ha aprovat amb un {nota}")
elif nota > 6.5 and nota <= 8:
    print(f"L'alumne ha tret un notable amb un {nota}")
elif nota > 8 and nota < 10:
    print(f"L'alumne ha tret un excelent amb un {nota}")
else:
    print(f"Nota no valida")