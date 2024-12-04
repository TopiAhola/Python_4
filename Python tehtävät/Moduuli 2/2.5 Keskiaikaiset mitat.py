'''Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

Yksi leiviskä on 20 naulaa.
Yksi naula on 32 luotia.
Yksi luoti on 13,3 grammaa.'''



print("Anna haluttu paino leivisköinä, nauloina ja luoteina:")

#tämä looppaa kunnes 3 numeroa annettu
while True:
    try:
        leiviskät = float(input("Leiviskät:"))
        naulat = float(input("Naulat:"))
        luodit = float(input("Luodit:"))

    except ValueError:
        print("Vain luvut kelpaavat!")

    else:
        break


#vanhojen mittojen painot grammoina
luoti_g = float(13.3)
naula_g = float(32 * luoti_g)
leiviskä_g = float(20 * naula_g)

#osapainot grammoina
leiviskä_m = leiviskät * leiviskä_g
naula_m = naulat * naula_g
luoti_m = luodit * luoti_g

#paino grammoina yhteensä
massa = leiviskä_m + naula_m + luoti_m
massa_kg = float(massa/1000)


#tulostus, kokeilen eri tapoja
print("Paino on:")
print(str(massa)+"g")
print(f"{massa_kg:.3f}Kg" )

