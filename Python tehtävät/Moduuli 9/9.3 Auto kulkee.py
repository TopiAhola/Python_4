'''Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.'''

class Auto:

    määrä = 0

    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

        Auto.määrä += 1

    def kulje(self, aika):

        d_matka = aika * self.nopeus
        self.matka = self.matka + d_matka

        return

#auto ajaa nopeudella 100km/h
auto2 = Auto("AAA-123", 150, 100, 0)

auto2.kulje(float(input("Anna ajoaika: ")))

print(f"Kuljettu matka: {auto2.matka}km")

