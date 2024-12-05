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
    active_game = ""
    games = {}
    #Game sisältää kaikki pelaajan tiedot
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        for icao, object2 in Airport.airports.items():
            self.airports[icao] = object2

        self.goals = {}

    #get_data palauttaa pelaajan tiedot dictionarynä   ##Tämä tehdään uusiksi site, että serveri varastoi tiedot dic mutta palauttaa listan
    #      lista = list(dict.values())
    def get_data (self):
        return_data = {
        "game_status": self.game_status,
        "message": self.message,
        "debugmessage": self.debugmessage,
        "name": self.name,
        "flight_type": self.flight_type,
        "destination": self.destination,
        "difficulty": self.difficulty,
        "start_money": self.start_money,
        "money": self.money,
        "money_gained": self.money_gained,
        "co2": self.co2,
        "money_gained_total": self.money_gained_total,
        "money_spent_total": self.money_spent_total,
        "distance": self.distance,
        "location": self.location.__dict__,
        "flights": self.flights}
        return_data["airports"] = []
        for icao5, object5 in self.airports.items():
            return_data["airports"].append(object5.__dict__)
        return_data["goals"] = []
        for icao6, object6 in self.goals.items():
            return_data["goals"].append(object6.__dict__)

        return return_data

    def start_and_goals(self):   #asettaa pelaajalle aloituskentän ja tavoitteet
        icao3, object3 = random.choice(list(Airport.airports.items())) #Satunnaisen kentän tiedot sijainniksi
        self.location = object3
        goals_icao = []
        while len(goals_icao) < 5:
            icao4, object4 = random.choice(list(Airport.airports.items()))
            if icao4 not in goals_icao and icao4 != self.location.icao:
                goals_icao.append(icao4)
                self.goals[icao4] = object4
                print(len(goals_icao))
                print(self.goals)
        print("Asetetaan tavoitteet:")
        for icao in goals_icao:
            self.airports[icao].goal = True
            print(self.airports[icao].name)

    def fly(self, flight_type, dest):
        dist = int(distance.distance((self.location.lat, self.location.lon), (self.airports[dest].lat, self.airports[dest].lon)).km)
        if flight_type == "SMALL":
            cost = dist*0.3
            co2 = dist*0.1
        elif flight_type == "NORMAL":
            cost = dist*0.2
            co2 = dist*0.2
        elif flight_type == "HIGH":
            cost = dist*0.1
            co2 = dist*0.3
        else:
            cost = dist  #oletuskerroin on 1
            co2 = dist   #oletuskerroin on 1

        self.money = self.money - cost
        self.money_spent_total = self.money_spent_total + cost
        self.co2 = self.co2 + co2
        self.location = Airport.airports[dest]

        if dest in self.goals:
            self.goals[dest].visited = True
            print("Saavutut tavoitteen")

        if self.airports[dest].visited == False:
            self.airports[dest].visited = True
            gain = self.airports[dest].gdp * 2  # Rahaa saa 2*gdp. Arvon muuttaminen vaikuttaa vaikeusasteeseen.
            self.money = self.money + gain
            self.money_gained = self.money_gained + gain
            self.money_gained_total = self.money_gained_total +gain
            print(f"Saat rahaa {gain}")

        self.message = f"Saavut lentokentälle {self.location.name}, saat rahaa {gain}"

    def goal_check(self): #Tarkistaa onko peli voitettu. Muokkaa game_status arvon "gamewon"
        gamewon = True
        for icao, object in self.goals.items():
            if object.visited == False:
                gamewon = False
        if gamewon == True:
            self.game_status = "gamewon"
            self.message = "Saavutit kaikki tavoitteet. Voitit pelin!"

    def money_check(self): #Tarkistaa onko peli hävitty. Muokkaa game_status arvon "gameover"
        if self.game_status == "gameinprogress":
            gameover = True
            for flight in self.flights:
                if flight["cost"]*0.1 < self.money: #Jos on varaa halvimpaan luokkaan
                    gameover = False

            if gameover == True:
                self.game_status = "gameover"
                self.message = "Sinulla ei ole varaa lentää. Hävisit pelin!"


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
        "money_gained": 0,
        "co2": 0,
        "money_gained_total": 0,
        "money_spent_total": 0,
        "distance": 0,
        "location": object,
        "flights": [],
        "airports": {},
        "goals": {}
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
    Game.active_game = name #Vaihtaa aktiivisen peliobjektin nimen perusteella

    return json.dumps(Game.games[Game.active_game].get_data())

@app.route('/newgame/<nimi>/<difficulty>')
def server_newgame(nimi, difficulty):
    #Alustaa uuden pelin. game_data muuttujat laitetaan oletusarvoihin ja lisätään pelaajan nimi:
    nimi_str = str(nimi)
    nimi = Game(**game_data_default)                                                #Määritellään pelaaja Game luokkaan oletus attribuuteilla
    Game.games[nimi_str] = nimi                                                      #Pelaajaoliota kutsutaan: Game.games[active_game]
    Game.active_game = nimi_str                                                     #Laitetaan luokkamuuttuja osoittamaan uusimpaan peliin
    Game.games[Game.active_game].name = nimi_str                                             #Asetetaan oikea nimi ja vaikeusaste
    Game.games[Game.active_game].difficulty = difficulty
    Game.games[Game.active_game].money = 2000
    Game.games[Game.active_game].start_money = 2000                            #Tämän pitää olla vaikeusasteen funktio
    #Game.games[Game.activeGame.name] = nimi                                    #Game.games dic sisältää kaikki pelit. Avaimena nimi.
    Game.games[Game.active_game].start_and_goals()                                          #Antaa pelaajalle sijainnin ja tavoitteet
    Game.games[Game.active_game].flights = Airport.airports[Game.games[Game.active_game].location.icao].flights  #Päivittää pelaajalle tarjolla olevat lennot.
    #Tähän voi lisätä jokerilentofunktion
    print(Game.games[Game.active_game].goals)
    print(Game.games)
    return json.dumps(Game.games[Game.active_game].get_data())                              #haetaan pelin tilanne game.get_data()


@app.route('/<flight_type>/<destination>')
def server_input(flight_type, destination):
    destination = destination.upper()                                                   #ICAO koodit on isolla kirjaimella
    flight_type = flight_type.upper()                                                   #Lentoluokka SMALL/NORMAL/HIGH
    Game.games[Game.active_game].fly(flight_type, destination)                                       #tekee lennon muutokset (lisää päästöjä, vähemmän rahaa, saapumispalkkio, )
    Game.games[Game.active_game].flights = Airport.airports[Game.games[Game.active_game].location.icao].flights #Päivittää pelaajalle tarjolla olevat lennot.
    #Tähän voi lisätä jokerilentofunktion
    Game.games[Game.active_game].goal_check()                        #TArkistaa onko pelaaja voittanut pelin. Palauttaa gamewon tai gameinprogress
    Game.games[Game.active_game].money_check()                       #Tarkistaa voiko pelaaja enää lentää. Palauttaa gameover tai gameinprogress kunhan peliä ei ole voitettu.

    return json.dumps(Game.games[Game.active_game].get_data())       #haetaan pelin tilanne game.get_data()

if True:
    app.run(use_reloader=True, host='127.0.0.1', port=3000)


