'''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä
alkuperäisen että karsitun listan.'''

#Listasta pitää tehdä kopio, jotta funktio ei muokkaa alkuperäistä listaa.


def parilliset(lista):
    lista2 = []
    for n in lista:
        if n % 2 == 0:
            lista2.append(n)

    return lista2

lista = []

print("Anna kokonaislukuja. Anna muu kuin kokonaisluku lajitellaksesi luvut.")

while True:
    try:
        lista.append(int(input("Anna kokonaisluku:  ")))

    except ValueError:
        break

print(f"Annetut luvut: {lista}")

print(f"Parilliset luvut:  {parilliset(lista)}")
