# Importit
import mysql.connector
import random
from geopy import distance

# Yhteys tietokantaan
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',
              "collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()



