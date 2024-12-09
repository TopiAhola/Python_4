from cgi import print_environ

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
# airport_default = {"goal": False, "visited": False, "icao": "", "name": "", "country": "", "lat": "","lon": "", "gdp": ""}
# flight_default = {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50","lat": "50.22", "lon": "20.22"}

##Luokat:

class Airport:
    airports = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        Airport.airports[self.icao] = self  #Lisätään luokkalistaan
        self.flights = []                   #Lisätään lentolista attr

    def create_flights(self): #Luo 3 lentoa lentokentältä.
        flights_all = [] #Tehdään lennot kaikille muille kentille
        for key, object in Airport.airports.items():
            if object != self:
                dist = int(distance.distance((self.lat, self.lon), (object.lat, object.lon)).km)
                cost = dist #OLETUSKERROIN TÄHÄN JOS HALUTAAN VÄHÄPÄÄSTOISEN LENNON KERROIN = 0.3
                co2 = dist #OLETUSKERROIN TÄHÄN JOS HALUTAAN VÄHÄPÄÄSTOISEN LENNON KERROIN = 0.1
                flight =  {"name": object.name, "country": object.country, "icao": object.icao, "cost": cost, "distance": dist, "co2": co2,"lat": object.lat, "lon": object.lon}
                flights_all.append(flight)
                #print(flight)
        #Järjestetään lennot etäisyyden mukaan ja syötetään 3 lähintä:
        flights_all = sorted(flights_all, key=lambda flight: flight["distance"])
        for n in range (0,3):
            self.flights.append(flights_all[n])

    def more_flights(self): #Luo paluulentoja lentokentiltä joilla ei plauuyhteyttä.
        for dest in self.flights:                       #Jokaista määränpäätä kohden.
            print(dest["icao"]),print(dest["name"])
            return_flight_exists = False
            for dest_flight in Airport.airports[dest["icao"]].flights: #Jos määränpään lentolistassa on paluulento...
                if dest_flight["icao"] == self.icao:
                    return_flight_exists = True

            if return_flight_exists == False: #Luodaan paluulento metodilla:
                Airport.airports[dest["icao"]].create_1_flight(self)

    def create_1_flight(self, object): #Luo self-objektille lennon argumentin objektiin.
        dist = int(distance.distance((self.lat, self.lon), (object.lat, object.lon)).km)
        cost = dist  # OLETUSKERROIN TÄHÄN JOS HALUTAAN VÄHÄPÄÄSTOISEN LENNON KERROIN = 0.3
        co2 = dist  # OLETUSKERROIN TÄHÄN JOS HALUTAAN VÄHÄPÄÄSTOISEN LENNON KERROIN = 0.1
        flight = {"name": object.name, "country": object.country, "icao": object.icao, "cost": cost, "distance": dist,"co2": co2, "lat": object.lat, "lon": object.lon}
        self.flights.append(flight)
        # print(flight)

################################
#Pääohjelma

def create_airports():
    sql1 = f"SELECT * FROM kentat"
    kursori.execute(sql1)
    vastaus = kursori.fetchall()
    for kentta in vastaus:
        kentta_kwargs = {"goal": False, "visited": False, "icao": kentta[1], "name": kentta[3], "country": kentta[18], "lat": kentta[4],"lon": kentta[5], "gdp": kentta[19]}
        Airport(**kentta_kwargs)

    #Testejä:
    #print(vastaus)
    #print(vastaus[0])
    #print(vastaus[1])
    #print(Airport.airports["EBBR"])

create_airports()
Airport.airports["EBBR"].create_flights()
Airport.airports["EBBR"].more_flights()
print(Airport.airports["EBBR"].flights)
print("testi1")
print(Airport.airports["EHAM"].flights)
print(Airport.airports["LFPG"].flights)
print(Airport.airports["EGLL"].flights)
print(Airport.airports["EFHK"].flights)

