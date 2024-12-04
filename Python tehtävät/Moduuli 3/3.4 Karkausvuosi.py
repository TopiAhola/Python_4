'''Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
Vuosi on karkausvuosi, jos se on jaollinen neljällä.
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.'''

vuosi = int(input("Anna vuosiluku: "))

# % antaa jakojäännöksen. Jos jakojäännös on 0 luku on tasan jaollinen.
# Toimii myös negatiivisilla numeroilla
if vuosi % 100 == 0 and vuosi % 400 == 0 or vuosi % 100 != 0 and vuosi % 4 == 0:
    print("Vuosi on karkausvuosi.")

else:
    print("Vuosi ei ole karkausvuosi.")