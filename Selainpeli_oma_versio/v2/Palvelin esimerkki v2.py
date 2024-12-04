##################################################
## Importit ##
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import json


###################################################
## Luokat ##

class Game:
    activeGame = []
    #Game sisältää kaikki pelaajan tiedot
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.debugmessage = "default"
        self.location = {"goal": False, "visited": True, "icao": "efhk", "name": "Helsinki", "country": "Suomi", "lat": "50.22","lon": "20.22", "gdp": "50"}
        self.message = "defaultviesti"

    #get_data palauttaa pelaajan tiedot dictionarynä
    def get_data (self):
        player_game_data = {}
        player_game_data["name"] = self.name
        player_game_data["difficulty"] = self.difficulty
        player_game_data["location"] = self.location
        player_game_data["message"] = self.message
        player_game_data["debugmessage"] = self.debugmessage
        return player_game_data

    def get_flights(self):
        pass

    def fly_testi(self, flight_type, destination):
        self.location = {"goal": False, "visited": False, "icao": "efhk", "name": "espoo", "country": "suomi", "lat": "50.22","lon": "20.22", "gdp": "0"}
        self.debugmessage = self.debugmessage +"fly_testi funktio" #Lisää stringin debug kentään kun funktio toimii


class Airports:
    #Kaikki lentokentät
    def __init__(self, ):
        pass


######################################
## Pääohjelma ##


######################################
## Flask ##
app = Flask(__name__)
CORS(app)

@app.route('/newgame/<name>/<difficulty>')
def server_newgame(name, difficulty):
    #Alustaa uuden pelin. game_data muuttujat laitetaan oletusarvoihin ja lisätään pelaajan nimi:

    game = Game(name, difficulty) #Määritellään pelaaja Game luokkaan
    Game.activeGame.append(game)  #Laitetaan pelaaja luokkamuuttujaan. pelaaja-objektia kutsutaan: Game.activeGame[0]
    server_return_data = game.get_data()

    return server_return_data


@app.route('/<flight_type>/<destination>')
def server_input(flight_type, destination):


    Game.activeGame[0].fly_testi(flight_type, destination) #tekee lennon muutokset
    vastaus = Game.activeGame[0].get_data() #hakee tiedot
    vastaus_json = json.dumps(vastaus)
    return vastaus_json


if True:
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


#######################################################
## Tietorakenne ##
'''
game_data = {
        "game_status": "gameinprogress/gameover/gamewon",
        "message": "default",
        "name": "default",
        "flight_type": "default",
        "destination": "default",
        # "total"-arvot on kertymä koko pelin ajalta. money_gained on viimeisimmän saapumisen lisäämä rahamäärä
        "difficulty": "hard?",
        "start_money": "1500",
        "money": "1500",
        "money_gained": "123",
        "co2": "50",
        "money_gained_total": "200",
        "money_spent_total": "100",
        "distance": "1000",
        # time, temperature, weather on reaaliaikaisia muuttujia joita ei tallenneta tietokantaan.
        "time": "12.00",
        "temperature": "20",
        "weather": "cloudy?",
        # Pelaajan sijainti, lentokentän tiedot:
        "location": {"goal": True, "visited": True, "icao": "efhk", "name": "helsinki", "country": "suomi",
                     "lat": "50.22", "lon": "20.22", "gdp": "0"},
        # lista tarjolla olevista lennoista:
        "flights": [{"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"},
                    {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50",
                     "lat": "50.22", "lon": "20.22"}
                    ],
        # lista KAIKISTA lentokentistä. Vieraillut ja tavoite kentät on osoitettu booleilla: goal ja visited True/False
        "airports": [
            {"goal": True, "visited": True, "icao": "efhk", "name": "helsinki", "country": "suomi", "lat": "50.22",
             "lon": "20.22", "gdp": "0"},
            {"goal": False, "visited": False, "icao": "efhk", "name": "espoo", "country": "suomi", "lat": "50.22",
             "lon": "20.22", "gdp": "0"},
            {"goal": True, "visited": False, "icao": "efhk", "name": "vantaa", "country": "suomi", "lat": "50.22",
             "lon": "20.22", "gdp": "0"}
            ]
    }
'''
