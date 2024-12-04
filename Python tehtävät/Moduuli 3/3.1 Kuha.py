'''Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.'''



pituus = float(input("Anna kuhan pituus senttimetreinä:"))


if pituus>=float(60):
    print("Onpa iso kuha. Voit nostaa sen.")
    exit()

if pituus>=float(37):
    print("Voit nostaa kuhan.")
    exit()


else:
    ero = float(37-pituus)
    print("Laske kuha takaisin järveen, se on "+str(ero)+"cm liian lyhyt.")
