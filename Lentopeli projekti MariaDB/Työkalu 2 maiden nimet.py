

import mysql.connector
parametrit = {
    "host" :'localhost',
    'database' :'flight_game',
    'user' : 'root',
    'password' : 'paskatietokanta'
            }

#haetaan maat tietokannasta
yhteys = mysql.connector.connect(**parametrit)

sql = f"SELECT iso_country, country_fi, municipality FROM kentat  "


print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print(tulos)










