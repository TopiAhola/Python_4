'''
Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys,
joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
'''




class Hissi:
    def __init__(self, alink, ylink ):
        self.alink = alink
        self.ylink = ylink
        self.kerros = alink

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Kerros {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Kerros {self.kerros}")

    def siirry_kerrokseen(self, kohde):
        while self.kerros != kohde:

            if self.kerros < kohde:
                self.kerros_ylös()

            if self.kerros > kohde:
                self.kerros_alas()

class Talo:

    def __init__(self, talo_alink, talo_ylink, hissien_määrä):
        self.talo_alink = talo_alink
        self.talo_ylink = talo_ylink
        self.hissien_määrä = hissien_määrä
        self.hissilista = []

        for n in range(0,hissien_määrä):
            self.hissilista.append( Hissi(talo_alink,talo_ylink, ) )

        print(f"Talossa {self} on {hissien_määrä} hissiä.")


    def aja_hissiä(self, hissi, kerros):
        self.hissilista[hissi].siirry_kerrokseen(kerros)

    def palohälytys(self):
        print("Palohälytys")
        for n in self.hissilista:
            n.siirry_kerrokseen(0)








talo1 = Talo(1, 10, 5)

#print(talo1.hissilista)

talo1.aja_hissiä( 2 , 10)
talo1.aja_hissiä(0, 10)
talo1.palohälytys()
