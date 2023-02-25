name = input("Qual o seu nome? ")
age = int(input("Prazer {}, qual a sua idade? ".format(name)))
next = age + 1
print("Legal {}, no seu próximo aniversário você fará {} anos.".format(name, next))
