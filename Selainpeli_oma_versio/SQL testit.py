import mysql.connector
import random
from geopy import distance

# Yhteys #
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',"collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()


# Tässä koodissa
# 1. Luodaan dic lentokenttien pohjalta
# 2. Luodaan kentille lentoyhteydet lähimmille kentille
# 3. Luodaan käänteiset lennot edellisille lennoille

# 4. Luodaan save_game funktio pelin tallentamiseksi tietokantaan. Pitää tuhota vanhat tiedot tietokannasta jotta tiedot ei kahdennu...
# 5. Load game funktio.

#Tietorakenteet:
# airport_default = {"goal": False, "visited": False, "icao": "efhk", "name": "vantaa", "country": "suomi", "lat": "50.22","lon": "20.22", "gdp": "10"}
# flight_default = {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50","lat": "50.22", "lon": "20.22"}


sql1 = f"SELECT * FROM kentat"
kursori.execute(sql1)
vastaus = kursori.fetchall()
print(vastaus)
