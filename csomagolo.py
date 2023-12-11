def papir():
    ures = 0
    szam1 = int(input("Kérem adjon meg egy negatív számot: "))
    szam2 = int(input("Kérem adjon meg egy másik negatív számot: "))

    if szam1 > szam2:
        ures = szam1
        szam1 = szam2
        szam2 = ures
    print("\tVégeredmény: ", end="")
    for i in range(szam1, szam2, 1):
        print(i, end="*")
    print(szam2, end="")
