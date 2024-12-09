from itertools import product

def Combinaisons():
    a = product(range(1, 7), repeat=5)
    
    C = 0
    for a in a:
        if sum(a) == 20:
            C += 1
    
    return C

b = Combinaisons()
print(f"Nombre de façons d'obtenir une somme de 20 avec 5 dés est : {b}")
