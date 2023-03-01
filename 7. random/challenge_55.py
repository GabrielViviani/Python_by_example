import random
num = random.randint(1,5)
pick = int(input("Escolha um número de 1 a 5: "))

if pick == num:
    print("Bom trabalho.")
elif pick > num:
    print("Alto demais.")
    pick = int(input("Escolha outro número: "))
    if pick == num:
        print("Correto.")
    else:
        print("Você perdeu.")
elif pick < num:
    print("Muito baixo.")
    pick = int(input("Escolha outro número: "))
    if pick == num:
        print("Correto.")
    else:
        print("Você perdeu.")    
