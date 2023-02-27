num = 10

while num > 0:
    print("Existem {} garrafas verdes na parede".format(num))
    print("{} garrafas verdes na parede".format(num))
    print("E se 1 garrafa caísse, ")
    num = num - 1
    answer = int(input("quantas garrafas sobrariam? "))

    if answer == num:
        print("Sobrarão {} garrafas na parede.".format(num))
    else:
        while answer != num:
            answer = int(input("Errado, tente novamente: "))
print("Não existem mais garrafas na parede.")