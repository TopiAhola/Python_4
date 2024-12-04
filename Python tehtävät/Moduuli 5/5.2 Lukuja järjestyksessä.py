'''Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä
suurimmasta alkaen. Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
antamalla sort-metodille argumentiksi reverse=True.'''

lista = []
try:
    luku = float(input("Anna luku. Anna jotain muuta kuin luku lopettaaksesi:  "))
except ValueError:
    exit()

while luku!="":
    try:
        lista.append(luku)
        luku = float(input("Anna luku:  "))


    except ValueError:
        break


print(f"Annetut luvut: {lista}")

#Lista käänteisessä suuruusjärjestyksessä:
lista.sort(reverse=True)
print(f"Viisi suurinta lukua: {lista[:5]}" )



