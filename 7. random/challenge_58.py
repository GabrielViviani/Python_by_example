import random

score = 0

for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    print("{} + {} = ".format(num1,num2))
    ans = int(input("Sua resposta: "))
    print()
    if ans == correct:
        score = score + 1
print("Você marcou {} de 5.".format(score))