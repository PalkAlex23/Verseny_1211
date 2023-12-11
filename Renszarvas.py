adatLista = []


class Renszarvas:
    def __init__(self, nev, magassag, hely, leiras):
        self.nev = nev
        self.magassag = int(magassag)
        self.hely = int(hely)
        self.leiras = leiras

    def __str__(self) -> str:
        return f"Neve: {self.nev}, magassága: {self.magassag}"

    def beolvasas(self):
        beFajl = open("fajlok/Mikulasszan.txt", "r", encoding="utf-8")
        beFajl.readline()
        sorok = beFajl.readlines()
        for sor in sorok:
            # tisztott sor
            tisztitottsor = sor.strip()
            # eldabarolás
            daraboltsor = tisztitottsor.split("@")
            # példányosítás
            csoporttag = Renszarvas(daraboltsor[0], daraboltsor[1], daraboltsor[2], daraboltsor[3])
            # belefűzöm az objektumokat a listába
            adatLista.append(csoporttag)
        beFajl.close()

    def kiir(self):
        for index in range(0, len(adatLista), 1):
            print(adatLista[index])
