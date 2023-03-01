import random

num = random.randint(1,10)

guess = int(input("Escolha um número de 1 a 10: "))

while guess != num:
    guess = int(input("Errou! Escolha outro número: "))

print("Correto!")