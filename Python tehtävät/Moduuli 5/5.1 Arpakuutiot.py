'''Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.'''

import random

nopat = int(input("Montako noppaa heitetään?  "))
lista = []
summa = int(0)

for luku in range(nopat):

    n = random.randint(1,6)
    summa = summa + n
    lista.append(n)


print(f"Heitot: {lista} ")
print(f"Yhteensä: {summa}")

