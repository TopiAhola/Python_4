'''Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.
Vihje: tutustu random.randint()-funktion käyttöön.'''

import random

numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)

luku1 = random.randint(1,6)
luku2 = random.randint(1,6)
luku3 = random.randint(1,6)
luku4 = random.randint(1,6)


print("Kolme numeroa väliltä 0-9:")
print(numero1, numero2, numero3)
print()
print("Neljä numeroa väliltä 1-6:")
print(luku1, luku2, luku3, luku4)

