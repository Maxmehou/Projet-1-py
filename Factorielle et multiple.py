n = 9
a = 1
for i in range(1, n + 1):
    a *= i

print(f"Factorielle de {n} (avec for) : {a}")


b = 1
i = 1
while i <= n:
    b *= i
    i += 1

print(f"Factorielle de {n} (avec while) : {b}")


print("\nRésultat pour les entiers de 1 à 50 :")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: MEHOU Maxime")
    elif i % 3 == 0:
        print(f"{i}: MEHOU")
    elif i % 5 == 0:
        print(f"{i}: Maxime")
    
