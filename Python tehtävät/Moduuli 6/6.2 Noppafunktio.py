'''Muokkaa edellistä funktiota siten, että funktio saa parametrinaan
nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä
esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen
nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
joka kysytään käyttäjältä ohjelman suorituksen alussa.'''


def noppa(tahkot):
    import random
    tulos=random.randint(1,tahkot)

    return tulos

tulos = int()
tahkot = int(input("Anna nopan tahkojen määrä:  "))
while tulos != tahkot:
    tulos=noppa(tahkot)
    print(tulos)

print("Ohjelma päättyy.")