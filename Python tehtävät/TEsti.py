'''
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun
taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat.

Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot.
Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja
Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

'''

class Julkaisu:
    def __init__ (self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__ (self, nimi, kirjoittaja, sivumaara):
        Julkaisu.__init__(self,nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

class Lehti(Julkaisu):
    def __init__ (self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja


kirja_1 = Kirja("nimi1", "pekka", 500)
lehti1 = Lehti("Sanomat", "myös pekka")
joku = Julkaisu("Julkkis")

print(Julkaisu, kirja_1, lehti1.nimi)

lista = [1,2,3,4,]
lista.append(1)
lista[4] = 55
print(lista)
print(len(lista))

