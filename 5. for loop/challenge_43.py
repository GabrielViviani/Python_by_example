way = str.lower(input("""
1- Cima
2- Baixo

Selecione a opção de contagem: """))

if way == "1" or way == "cima":
    num = int(input("Informe o número do ponto de chegada: "))
    for i in range(0,num+1):
        print(i)

elif way == "2" or way == "baixo":
    num = int(input("Selecione um número menor do que 20: "))
    for i in range(20, num-1, -1):
        print(i)

else:
    print("Nenhuma opção válida selecionada.")
