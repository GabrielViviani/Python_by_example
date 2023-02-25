answer = str.lower(input("Está chovendo hoje? Responda com 'sim' ou 'não' "))

if answer == "sim":
    answer2 = str.lower(input("E está ventando? "))
    if answer2 == "sim":
        print("Está ventando muito para levar um guarda-chuva")
    elif answer2 == "não":
        print("Então leve um guarda-chuva.")
elif answer == "não":
    print("Aproveite seu dia!")