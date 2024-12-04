'''Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi
kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne
listarakenteeseen. Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan
allekkain samassa järjestyksessä kuin ne syötettiin. käytä for-toistorakennetta
nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.'''


kaupungit = []

for kaupunki in range(0,5):
    kaupungit.append(input("Anna kaupunki: "))

for kaupunki in kaupungit:
    print(kaupunki)

