total = 0

for i in range(0,5):
    num = int(input("Insira um número: "))
    ans = input("Você gostaria de adicionar esse número ao total?\n (S / N): ")

    if ans == "S":
        total = total + num
    
print("O total da soma foi: {}".format(total))