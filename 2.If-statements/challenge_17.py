age = int(input("Qual a sua idade? "))

if age >= 18:
    print("Você pode votar.")
elif age == 17:
    print("Você pode dirigir.")
elif age == 16: 
    print("Você pode comprar um bilhete da loteria.")
elif age < 16:
    print("Você pode brincar de pique-pega.")