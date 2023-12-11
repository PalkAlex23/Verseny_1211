from random import randint
lista = []
listaHarmadik = []


def ajandek():
    kiFajl = open("fajlok/csomagolopapir.txt", "w", encoding="utf-8")
    print("6. feladat")
    kiFajl.write("6. feladat\n")
    for i in range(1, 20):
        szam = randint(-10, 80)
        lista.append(szam)

    for index in range(0, len(lista)):
        if index % 3 == 2:
            print("\t"+str(lista[index]), end=" ")
            listaHarmadik.append(lista[index])
            kiFajl.write(str(lista[index])+"\n")
    return listaHarmadik
