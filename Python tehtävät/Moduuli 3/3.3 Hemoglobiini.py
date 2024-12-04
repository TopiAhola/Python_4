'''Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.'''


#Vaihtoehdot on m, n tai exit. Muuttaa syötteen pieneksi kirjaimeksi.
sukupuoli=str()
while sukupuoli!=str("m") or sukupuoli!=str("n"):
    sukupuoli = str(input("Anna sukupuoli: m = mies, n = nainen, exit = sulje ohjelma: ")).lower()


    if(sukupuoli=="m") or (sukupuoli=="n"):

        break

    if(sukupuoli=="exit"):
        exit()


print()


#Tämä hyväksyy vain floatteja hemoglobiiniarvoksi
while True:
    try:
        hemoglobiini = float(input("Anna hemoglobiiniarvo g/l: "))

    except ValueError:
        print("Hemoglobiiniarvo pitää olla numero!")

    else:
        break

print()



if sukupuoli=="n" and hemoglobiini<117 or sukupuoli=="m" and hemoglobiini<134:
     print("Hemoglobiiniarvo on alhainen.")
     exit()

elif (sukupuoli=="n" and hemoglobiini>175 or sukupuoli=="m" and hemoglobiini>195):
    print("Hemoglobiiniarvo on korkea.")
    exit()

else:
    print("Hemoglobiiniarvo on normaali.")
    exit()