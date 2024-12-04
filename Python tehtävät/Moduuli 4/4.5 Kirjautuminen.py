'''Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. Jos jompikumpi tai molemmat
ovat väärin, tunnus ja salasana kysytään uudelleen. Tätä jatketaan kunnes kirjautumistiedot ovat oikein
tai väärät tiedot on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä
Pääsy evätty. (Oikea käyttäjätunnus on python ja salasana rules).'''


yritys = int(1)
tunnus = "python"
salasana = "rules"


while yritys < 6:
    tunnus_input = input("Anna käyttäjätunnus:  ")
    salasana_input = input("Anna salasana:  ")
    yritys += 1

    if tunnus_input == tunnus and salasana_input == salasana:
        print("Tervetuloa")
        break
else:
    print("Pääsy evätty.")

