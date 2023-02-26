choice = int(input("""
1) Quadrado
2) Triângulo
Escolha uma opção: """))

if choice == 1:
    length = float(input("Qual o tamanho do lado? "))
    area = length**2
    print("A área do quadrado é {}".format(area))

elif choice == 2:
    base = float(input("Informe o tamanho da base: "))
    height = float(input("Informe a altura: "))
    area2 = base * height / 2
    print("A área do triângulo é {}".format(area2))

else:
    print("Nenhuma opção válida selecionada, terminando o programa.")