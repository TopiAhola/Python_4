########################################################################################
## Importit ##
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import json
import random
from geopy import distance

#########################################################################################
## Luokat ##

#Game luokka:
class Game:
    activeGame = object
    games = {}
    #Game sisältää kaikki pelaajan tiedot
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        for icao, object2 in Airport.airports.items():
            self.airports.append(object2.__dict__)

    #get_data palauttaa pelaajan tiedot dictionarynä
    def get_data (self):
        player_game_data = self.__dict__ #palauttaa pelaajan tiedot dic
        return player_game_data

    def start_and_goals(self):   #asettaa pelaajalle aloituskentän ja tavoitteet
        icao, object3 = random.choice(list(Airport.airports.items())) #Satunnaisen kentän tiedot sijainniksi
        self.location = object3.__dict__
        goals_icao = []
        while len(goals_icao) < 5:
            icao, object4 = random.choice(list(Airport.airports.items()))
            if icao not in goals_icao and icao != self.location["icao"]:
                goals_icao.append(icao)
                self.goals.append(object4.__dict__)
        print("Asetetaan tavoitteet:")
        for airport in self.airports:
            if airport["icao"] in goals_icao:
                airport["goal"] = True
                print(airport["name"])

    def fly_testi(self, flight_type, destination):
        self.location = Airport.airports[destination].__dict__    #Pitääkö olla dict vai riittääkö get_datassa sisällä oleva __dict__ ???
        self.debugmessage = self.debugmessage +"fly_testi_funktio," #Lisää stringin debug kentään kun funktio toimii

    def goal_check(self): #Tarkistaa onko peli voitettu. Muokkaa game_status arvon "gamewon"
        pass

    def money_check(self): #Tarkistaa onko peli hävitty. Muokkaa game_status arvon "gameover"
        pass

############################################################
## Airport luokka
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
                cost = dist #OLETUSKERROIN TÄHÄN JOS HALUTAAN VÄHÄPÄÄSTOISEN LENNON KERROIN = 0.3, HALVIN = 0.1
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
            #print(dest["icao"]),print(dest["name"])
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



##################################################################################################################
## Pääohjelma ##

## Tietokanta ##
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',"collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

## Funktiot

def create_airports():
    sql1 = f"SELECT * FROM kentat"
    kursori.execute(sql1)
    vastaus = kursori.fetchall()
    for kentta in vastaus:
        kentta_kwargs = {"goal": False, "visited": False, "icao": kentta[1], "name": kentta[3], "country": kentta[18], "lat": kentta[4],"lon": kentta[5], "gdp": kentta[19]}
        Airport(**kentta_kwargs)

## Pääohjelman koodi: ?
create_airports()                                  #Luodaan kentät
for icao, object1 in Airport.airports.items():     #Luodaan alustavat lennot
    object1.create_flights()
for icao, object1 in Airport.airports.items():     #Luodaan paluulennot
    object1.more_flights()

#######################################################
## Tietorakenne ##
#Pelaajan aloitusarvot ilman satunnaistamista:
game_data_default = {
        "game_status": "gameinprogress",
        "message": "default",
        "debugmessage": "default, ",
        "name": "default",
        "flight_type": "default",
        "destination": "default",
        "difficulty": "default",
        "start_money": 1500,
        "money": 1500,
        "money_gained": 12,
        "co2": 0,
        "money_gained_total": 0,
        "money_spent_total": 0,
        "distance": 0,
        "location": {"goal": True, "visited": True, "icao": "EFHK", "name": "helsinki", "country": "suomi", "lat": "50.22", "lon": "20.22", "gdp": "0"},
        "flights": [],
        "airports": [],
        "goals": []
}

#Lentokentän ja lennon tietorakenne:
airport_default = {"goal": False, "visited": False, "icao": "efhk", "name": "vantaa", "country": "suomi", "lat": "50.22","lon": "20.22", "gdp": "10"}
flight_default = {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50","lat": "50.22", "lon": "20.22"}
##################################################################################################################
## Flask ##
# Flask serveri pitää olla viimeisenä koodissa jotta muuttujat ja funktiot on määritelty.
app = Flask(__name__)
CORS(app)

@app.route('/loadgame/<name>')
def server_loadgame(name):
    Game.activeGame = Game.games[name] #Vaihtaa aktiivisen peliobjektin nimen perusteella
    load_game_data = Game.activeGame.get_data() #Palauttaa uuden aktiivisen pelin tiedot
    return load_game_data

@app.route('/newgame/<name>/<difficulty>')
def server_newgame(name, difficulty):
    #Alustaa uuden pelin. game_data muuttujat laitetaan oletusarvoihin ja lisätään pelaajan nimi:
    game = Game(**game_data_default) #Määritellään pelaaja Game luokkaan oletus attribuuteilla
    game.name = name                #Asetetaan oikea nimi ja vaikeusaste
    game.difficulty = difficulty
    game.money = game.start_money = 2000   # Tämän pitää olla vaikeusasteen funktio
    Game.activeGame = game              #Pelaajaoliota kutsutaan: Game.activeGame
    Game.games[game.name] = game        #Game.games dic sisältää kaikki pelit. Avaimena nimi.
    game.start_and_goals()                  #Antaa pelaajalle sijainnin ja tavoitteet
    game.flights = Airport.airports[game.location["icao"]].flights #Päivittää pelaajalle tarjolla olevat lennot.

    return json.dumps(game.get_data()) #haetaan pelin tilanne game.get_data()


@app.route('/<flight_type>/<destination>')
def server_input(flight_type, destination):
    destination = destination.upper() #ICAO koodit on isolla kirjaimella
    flight_type = flight_type.upper()
    Game.activeGame.fly_testi(flight_type, destination) #tekee lennon muutokset (lisää päästöjä, vähemmän rahaa, saapumispalkkio, )
    Game.activeGame.flights = Airport.airports[Game.activeGame.location["icao"]].flights #Päivittää pelaajalle tarjolla olevat lennot.
    Game.activeGame.goal_check() #TArkistaa onko pelaaja voittanut pelin. Palauttaa gamewon tai gameinprogress
    Game.activeGame.money_check() #Tarkistaa voiko pelaaja enää lentää. Palauttaa gameover tai gameinprogress kunhan peliä ei ole voitettu.

    return json.dumps(Game.activeGame.get_data()) #haetaan pelin tilanne game.get_data()

if True:
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


