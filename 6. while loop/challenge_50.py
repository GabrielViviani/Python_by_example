num = int(input("Insira um número entre 10 e 20: "))

while num < 10 or num > 20:
    if num < 10:
        print("Baixo demais")
    else:
        print("Alto demais")

    num= int(input("Tente de novo: "))
print("Obrigado.")