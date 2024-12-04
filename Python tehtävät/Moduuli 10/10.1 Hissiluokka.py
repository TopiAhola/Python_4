'''Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja
ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen,
kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.

Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat
hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa
hissi sen jälkeen on.
Testaa luokkaa siten, että teet pääohjelmassa hissin ja
käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.'''


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


hissi1 = Hissi(1, 10, )

#testausta varten:
#hissi1.siirry_kerrokseen(int(input("Anna kerros: ")))

hissi1.siirry_kerrokseen(10)
hissi1.siirry_kerrokseen(1)