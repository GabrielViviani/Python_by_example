compnum = 50
guess = int(input("Chute um número: "))
count = 1

while guess != compnum:
    if guess > compnum:
        guess = int(input("Alto demais, tente outro número: "))
        
    else:
        guess = int(input("Muito baixo, tente outro número: "))
        count = count + 1
print("Parabéns, você precisou de {} tentativas.".format(count))