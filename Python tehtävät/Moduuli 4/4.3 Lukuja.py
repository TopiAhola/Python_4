'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen
saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.'''

#Listan luominen pitää laittaa silmukan ulkopuolelle, muuten resetoituu silmukan mukana.

lista = []
luku = float()
while True:
    try:
        luku = float(input("Anna luku: "))
        lista.extend([luku])
        print(lista)

    except ValueError:
        break


#Etsitään listasta isoin ja pienin luku:
max = max(lista)
min = min(lista)

print(f"Suurin luku on: {max} Pienin luku on: {min}")




