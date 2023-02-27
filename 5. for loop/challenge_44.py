ppl = int(input("Quantas pessoas serão convidadas para a festa? "))

if ppl < 10:
    for i in range(0,ppl):
        name = input("Insira o nome do convidado: ")
        print("{} foi convidado.".format(name))

elif ppl >= 10:
    print("Gente demais.")