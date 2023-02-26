import math
radius = float(input("Insira o raio do círculo: "))
depth = float(input("Insira a profundidade: "))
volume = round((math.pi*radius**2)*depth,3)

print("O volume total é:",volume)