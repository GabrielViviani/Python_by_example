num1 = int(input("Insira um número: "))
soma = num1
ans = str.lower(input("Deseja adicionar outro número? \n (Sim / Não) \n "))

while ans == "sim":
    num2 = int(input("Insira mais um número: "))
    soma = soma + num2
    ans = str.lower(input("Quer adicionar mais um número? "))

print("O total foi: {}".format(soma))