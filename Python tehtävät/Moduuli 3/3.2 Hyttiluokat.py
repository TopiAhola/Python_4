'''Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen
alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.

LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.'''

#kysytään srt ja muutetaan pieniksi kirjaimiksi
luokka = str(input("Anna hyttiluokka")).casefold()


if luokka==str("lux"):
    print("Parvekkeellinen hytti yläkannella.")

elif luokka==str("a"):
    print("Ikkunallinen hytti autokannen yläpuolella.")

elif luokka==str("b"):
    print("Ikkunaton hytti autokannen yläpuolella.")

elif luokka==str("c"):
    print("Ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")

