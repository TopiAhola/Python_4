#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

print("Anna kolme kokonaislukua.")

#Tämä looppaa kunnes kolme kokonaislukua syötetty


while True:
    try:
        luku1 = int(input("Luku 1:"))
        luku2 = int(input("Luku 2:"))
        luku3 = int(input("Luku 3:"))

    except ValueError:
        print("Vain kokonaisluvut kelpaavat!")

    else:
        break


#Laskutoimitukset
summa = luku1+luku2+luku3
tulo = luku1*luku2*luku3
keskiarvo = summa/3

#Tulostus
print("Lukujen summa on: "+str(summa))
print("Lukujen tulo on: " + str(tulo))
print("Lukujen keskiarvo on: " + str(keskiarvo))

