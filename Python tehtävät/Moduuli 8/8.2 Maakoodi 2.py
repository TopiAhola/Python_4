'''Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja
tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä
lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.'''

import mysql.connector
#yhteys
parametrit = {
    "host" :'localhost',
    'database' :'flight_game',
    'user' : 'topi',
    'password' : ''}
yhteys = mysql.connector.connect(**parametrit)



maakoodi = input("Anna maakoodi: ")

#sql koodi
sql = f"select type, count(*) from airport where iso_country = '{maakoodi}' group by type"

print(f" \n {sql} \n")

#syöte ja fetch
#tämä antaa dictionary-tuple tms.
#
cursor = yhteys.cursor()
cursor.execute(sql)
tulos = cursor.fetchall()

#Jokainen rivi on tuple
#tämä avaa tuplet ja selventää typen
for a in tulos:
    x = a[0]
    y = a[1]
    if x == "closed":
        x = "Closed"
    elif x == "heliport":
        x = "Heliport"
    elif x == "small_airport":
        x = "Small Airport"
    elif x == "medium_airport":
        x = "Medium Airport"
    elif x == "large_airport":
        x = "Large Airport"
    elif x == "seaplane_base":
        x = "Seaplane Base"
    elif x == "balloonport":
        x = "Balloon Port"
    print(x, y)


''' 
Eri lentokenttätyypit:
             balloonport    |
|      451 | large_airport  |
|     1100 | seaplane_base  |
|     4740 | medium_airport |
|     8675 | closed         |
|    17650 | heliport       |
|    38291 | small_airport '''