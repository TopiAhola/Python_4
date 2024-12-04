'''Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia
vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten,
että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös
luvulla 3 tai luvulla 7.'''



luku = int(input("Anna kokonaisluku:  "))

#Aloitetaan kakkosella, koska kaikki luvut ovat jaollisia ykkösellä.
n = int(2)

while n<luku:
    #Jos jakojäännös on 0, luku on jaollinen muuttujalla n.
    if luku % n == 0:
        print(f"On jaollinen luvulla {n}")
        print(f" {luku} / {n} = {luku/n}")
        print("Luku ei ole alkuluku")
        break

    #Jos jakojäännös ei ole 0 lisätään muuttujan n arvoa yhdellä.
    else:
        print(f"Kokeiltu jakaa: {n}")
        n = n + 1

else:
    print(f"Luku {luku} on alkuluku!")

print("Ohjelma päättyy.")