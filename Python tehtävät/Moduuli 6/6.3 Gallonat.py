'''Kirjoita funktio, joka saa parametrinaan bensiinin määrän
Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.'''

def gallona_litra(gallonat):
    litrat = float(gallonat * 3.785)
    return litrat

#Tämä palauttaa negatiivisen arvon lopetettaessa... pitäisi lopettaa heti.

print("Anna määriä gallonoina. Anna negatiivinen määrä lopettaaksesi.")
gallonat = float()
while True:
    try:
        gallonat = float(input("Anna gallonat:  "))

        if gallonat < 0:
            break

        else:
            litrat = gallona_litra(gallonat)
            print(f"{gallonat} gallonaa on {litrat} litraa. ")

    except ValueError:
        print("Pitää olla luku. Anna negatiivinen luku lopettaaksesi")


print("Ohjelma päättyy.")