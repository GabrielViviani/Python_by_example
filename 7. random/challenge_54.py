import random

game = random.choice(["cara","coroa"])

user = str.lower(input("Escolha um:\n Cara \n Coroa\n  "))

if user == game:
    print("Você venceu!")
else:
    print("Que azar!")
print("O computador escolheu {}".format(game))