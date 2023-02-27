name = input("Quem você gostaria de convidar para a festa? ")
print("{} foi convidado.".format(name))
ans = str.lower(input("Gostaria de convidar mais alguém? (Sim / Não)\n "))
count = 1

while ans == "sim":
    name = input("Quem você gostaria de convidar para a festa? ")
    print("{} foi convidado.".format(name))
    ans = str.lower(input("Gostaria de convidar mais alguém? (Sim / Não)\n "))
    count = count + 1

print("Foram convidadas {} pessoas.".format(count))