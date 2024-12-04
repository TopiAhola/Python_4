#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

print("Anna kolme kokonaislukua.")

luku1=int(input("Luku 1:"))
luku2=int(input("Luku 2:"))
luku3=int(input("Luku 3:"))


summa = luku1+luku2+luku3
tulo = luku1*luku2*luku3
keskiarvo = summa/3

print("Lukujen summa on: "+str(summa))
print("Lukujen tulo on: " + str(tulo))
print("Lukujen keskiarvo on: " + str(keskiarvo))

