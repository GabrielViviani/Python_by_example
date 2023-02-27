name = input("Insira seu nome: ")
num = int(input("Insira um número menor que 10: "))


if num < 10:
    for i in range(0, num):
        print(name)

elif num > 10:
    for i in range(0,3):
        print("Alto demais")
