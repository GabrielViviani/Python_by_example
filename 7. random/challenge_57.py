import random

num = random.randint(1,10)

guess = int(input("Escolha um número de 1 a 10: "))

while guess != num:

    if guess > num:
        guess = int(input("Muito alto! Escolha outro número: "))
        
    elif guess < num:
        guess = int(input("Muito baixo! Escolha outro número: "))
    
print("Correto!")