'''Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa
tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)'''


lentoasemat = {
"EFAA": "Aavahelukka Airport",
"EFAH":"Ahmosuo Airport",
"EFAL":"Alavus Airfield",
"EFEJ":"Jorvin Hospital Heliport",
}

def uusi_lentoasema():
    uusi_ICAO = input("Anna uuden lentoaseman ICAO-koodi:  ")
    uusi_nimi = input("Anna uuden lentoaseman nimi:  ")

    lentoasemat [uusi_ICAO] = uusi_nimi

    print(f"Lisätty {uusi_ICAO} {uusi_nimi} \n")

    return

def haku_lentoasema(icao):
    if icao in lentoasemat:
        print(f"{icao} {lentoasemat[icao]} ")
    else:
        print("Lentoasemaa ei löydy.\n")

    return





while True:
    try:
        print(f"Lentoasemia tallennettu {(len(lentoasemat))} kappaletta.")
        vaihtoehto = int(input(f"Anna vaihtoehdon numero: \n 1 = Syötä uusi lentoasema \n 2 = Hae lentoasema \n 3 = Tulosta kaikki lentoasemat \n 4 = Lopeta \n"))

    except ValueError:
        print("Valitse vaihtoehto 1-3")

    if vaihtoehto == 1:
        uusi_lentoasema()

    if vaihtoehto == 2:
        icao = input("Anna ICAO koodi: ")
        haku_lentoasema(icao)

    if vaihtoehto == 3:
        print(f"{lentoasemat} \n")

    if vaihtoehto == 4:
        print("Lopetetaan.")
        break

else:
    exit