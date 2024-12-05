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

class Game:
    activeGame = object
    games = {}
    #Game sisältää kaikki pelaajan tiedot
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    #get_data palauttaa pelaajan tiedot dictionarynä
    def get_data (self):
        player_game_data = self.__dict__ #palauttaa pelaajan tiedot dic
        return player_game_data

    def get_flights(self):
        #
        pass

    def fly_testi(self, flight_type, destination):
        self.location = {"goal": False, "visited": False, "icao": "efhk", "name": "espoo", "country": "suomi", "lat": "50.22","lon": "20.22", "gdp": "0"}
        self.debugmessage = self.debugmessage +"fly_testi_funktio," #Lisää stringin debug kentään kun funktio toimii

#Airport testi luokka: 
class Airport:
    airports = {}

    def __init__(self, icao, flights):
        self.icao = icao
        Airport.airports[self.icao] = self #Lisätään luokkalistaan
        self.flights = flights



##################################################################################################################
## Pääohjelma ##

## Tietokanta ##
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',"collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

## Funktiot
def get_airports():
    #Hakee kentät tietokannasta dictionaryyn.
    pass

#Toimii :)
testilista = [ {"name": "testinimi", "country": "testi1", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50"}]
testikentta = Airport("efhk",testilista )

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
        "location": {"goal": True, "visited": True, "icao": "efhk", "name": "helsinki", "country": "suomi", "lat": "50.22", "lon": "20.22", "gdp": "0"},
        "flights": [{"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50", "lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50","lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50","lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50","lat": "50.22", "lon": "20.22"}
                    ],
        "airports": [   ]}

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
    game.money = 2000               # Tämän pitää olla vaikeusasteen funktio
    Game.activeGame = game          #Pelaajaoliota kutsutaan: Game.activeGame
    Game.games[game.name] = game    #Game.games dic sisältää kaikki pelit. Avaimena nimi.
    ## Kesken ##
    # 1. Haetaan lentokentät 2. määritetään tavoitteet 3. määritetään aloituskenttä
    # 4. syötetään "airports" dic game.airports attribuuttiin ja aloitus game.location
    # 5. luodaan lennon pelaajan sijainnin perusteella 6. syötetään lennot game.flights attribuuttiin.

    server_return_data = game.get_data() #haetaan pelin tilanne game.get_data()
    return server_return_data


@app.route('/<flight_type>/<destination>')
def server_input(flight_type, destination):
    destination = destination.upper() #ICAO koodit on isolla kirjaimella
    flight_type = flight_type.upper()
    Game.activeGame.fly_testi(flight_type, destination)#1.tekee lennon muutokset (lisää päästöjä, vähemmän rahaa, saapumispalkkio, )

    # 2. haetaan uudet lennot airports luokasta ja tallenetaan Game.activeGame.flights attribuuttiin
    # Tämä olisi helpompi jos game.location olisi airport olio...
    Game.activeGame.flights = Airport.airports[Game.activeGame.location["icao"]].flights
    vastaus = Game.activeGame.get_data() #hakee tiedot
    vastaus_json = json.dumps(vastaus)
    return vastaus_json

if True:
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


