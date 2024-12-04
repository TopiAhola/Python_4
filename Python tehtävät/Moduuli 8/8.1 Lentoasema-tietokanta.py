'''Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.'''


import mysql.connector

parametrit = {
    "host" :'localhost',
    'database' :'flight_game',
    'user' : 'topi',
    'password' : ''}
yhteys = mysql.connector.connect(**parametrit)
cursor = yhteys.cursor()

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = f"SELECT name, municipality from airport where ident = '{icao}'  "
print(sql)
cursor.execute(sql)
tulos = cursor.fetchall()
#print(tulos)

for rivi in tulos:
    print(f"Lentokenttä: {rivi[0]}")
    print(f"Kunta: {rivi[1]}")


