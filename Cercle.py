import matplotlib.pyplot as C

def Cercle():
    R = float(input("Entrez le rayon du cercle : "))

    fig, a = C.subplots()

    cercle = C.Circle((0, 0), R, color='red', fill=False)

    a.add_artist(cercle)

    a.set_xlim(-R - 1, R + 1)
    a.set_ylim(-R - 1, R + 1)
    a.set_aspect('equal')  

    a.set_title(f"Cercle de rayon {R}")
    C.xlabel("X")
    C.ylabel("Y")
    C.grid(True)
    C.show()

Cercle()
