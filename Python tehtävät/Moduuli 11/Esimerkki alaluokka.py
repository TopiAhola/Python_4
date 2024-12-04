class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kuukausipalkka: {self.kuukausipalkka}")


työntekijät = []
työntekijät.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
työntekijät.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
työntekijät.append(Työntekijä("Pekka", "Puro"))
työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))

for t in työntekijät:
    t.tulosta_tiedot()

#Tässä on useampi yläluokka:
#Huomaan että self annetaan argumentiksi kun yläluokka määritetään luokan nimen kautta eikä super(). -funktion kautta...


class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus


class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino


class Polkupyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus, paino, vaihteet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)

        self.vaihteet = vaihteet


pp = Polkupyörä(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)