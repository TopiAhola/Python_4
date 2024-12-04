'''Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin
kauan kunnes tulee kuutonen.
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.'''

def noppa():
    import random
    tulos=random.randint(1,6)

    return tulos

tulos = int()
while tulos!= 6:
    tulos=noppa()
    print(tulos)

print("Ohjelma päättyy.")