name = input("Insira seu primeiro nome: ")

if len(name) < 5:
    surname = input("Insira seu sobrenome: ")
    fullname = name + surname
    print(fullname.upper())
elif len(name) >= 5:
    print(name.lower())