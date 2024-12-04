'''Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän
ICAO-koodit. Ohjelma ilmoittaa lentokenttien välisen etäisyyden
kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.

Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.'''

#importit
import mysql.connector
from geopy import distance

#yhteys tietokantaan
parametrit = {"host" :'localhost', 'database' :'flight_game', 'user' : 'topi','password' : ''}
yhteys = mysql.connector.connect(**parametrit)

print("Anna kahden lentokentän ICAO-koodi.")
icao1 = input("Lentokenttä 1: ")
icao2 = input("Lentokenttä 2: ")

#Haetaan koordinaatit
sql1= f"select longitude_deg, latitude_deg from airport where ident ='{icao1}'  "
sql2= f"select longitude_deg, latitude_deg from airport where ident ='{icao2}' "

#pitääkö kursori nollata välissä? Testataan. Ei tarvitse.
kursori = yhteys.cursor()

kursori.execute(sql1)
tulos1 = kursori.fetchall()

kursori.execute(sql2)
tulos2 = kursori.fetchall()

kursori.close()

print(tulos1)
print(tulos2)

# Missä formaatissa koordinaatit pitää olla?
# longitude, latitude

distance = distance.distance(tulos1, tulos2).km
print(f"Lentokenttien etäisyys on {distance:.1f} km" )