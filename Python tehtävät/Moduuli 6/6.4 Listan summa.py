'''Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan.
Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
ja tulostat sen palauttaman summan.'''



def lista_summa(lista):
    summa = int(sum(lista))
    return summa


lista = []
luku = int()
print("Anna kokonaislukuja. Anna tyhjä tai muu merkki laskeaksesi luvut yhteen.")

while True:
    try:
        lista.append(int(input("Anna kokonaisluku: ")))

    except ValueError:
        break

print(lista)
summa = lista_summa(lista)
print(f"Lukujen summa on {summa}")



