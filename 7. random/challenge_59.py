import random
pc = random.choice(["laranja", "azul", "verde", "preto", "cinza"])
ans = str.lower(input("Escolha uma cor entre - laranja, azul, verde, preto ou cinza \n Sua escolha: "))

while ans != pc:
    if pc == "laranja":
        ans = str.lower(input("KKKKK tá precisando de um laranja pra te ajudar? "))
    elif pc == "azul":
        ans = str.lower(input("Vamo logo que eu tô azul de fome. "))
    elif pc == "verde":
        ans = str.lower(input("Resposta imatura... meio verde... "))
    elif pc == "preto":
        ans = str.lower(input("Tô quase tendo teto preto de esperar. "))
    else:
        ans = str.lower(input("Agiliza aí, o céu tá meio cinza, vai chover! "))
print("Bom trabalho!")