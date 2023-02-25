color = str.lower(input("Qual a sua cor favorita? "))

if color == "vermelho":
    print("Eu também gosto de vermelho.")
else:
    print("Eu não gosto de {}, prefiro vermelho.".format(color))