## Importit ##
from flask import Flask, request
from flask_cors import CORS
import mysql.connector
import json
import random
from geopy import distance

##################################################################################################################
## Luokat ##

#Game luokka:
class Game:
    active_game = ""
    games = {}
    #Game sisältää kaikki pelaajan tiedot
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.airports = {}
        self.create_airports()                      # Luodaan kentät game objektille
        for icao, object1 in self.airports.items():  # Luodaan alustavat lennot
            object1.create_flights(self)
        for icao, object1 in self.airports.items():  # Luodaan paluulennot
            object1.return_flights(self)

        self.goals = {}

        #for icao, object2 in Airport.airports.items():   Turhaa koodia???
            #self.airports[icao] = object2

    def create_airports(self):
        sql1 = f"SELECT * FROM kentat"
        kursori.execute(sql1)
        vastaus = kursori.fetchall()
        for kentta in vastaus:
            kentta_kwargs = {"goal": False, "visited": False, "icao": kentta[1], "name": kentta[3],
                             "country": kentta[18], "lat": kentta[4], "lon": kentta[5], "gdp": kentta[19], "db_saved": False}
            Airport(self, **kentta_kwargs)



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

    def set_difficulty(self, difficulty): #Asettaa vaikeusaste ja raha attribuutit helppo/normaali/vaikea 1000/1500/2000e
        self.difficulty = difficulty
        if difficulty == "helppo":
            self.money = 2000
            self.start_money = 2000
        elif difficulty == "normaali":
            self.money = 1500
            self.start_money = 1500
        elif difficulty == "vaikea":
            self.money = 1000
            self.start_money = 1000
        else:
            self.money = 500
            self.start_money = 500
        print("Vaikeusaste, aloitusrahat:", self.difficulty, self.start_money)

    def start_and_goals(self):   #Asettaa pelaajalle aloituskentän, sijainnin ja tavoitteet
        icao3, object3 = random.choice(list(self.airports.items())) #Satunnaisen kentän tiedot sijainniksi
        self.location = object3 #Asetetaan sijainti
        self.flights = object3.flights #Annetaan sijainnin lennot pelaajan lennoiksi
        self.airports[self.location.icao].visited = True #Pelaaja on käynyt aloituskentällä
        goals_icao = []
        while len(goals_icao) < 5:
            icao4, object4 = random.choice(list(self.airports.items()))
            if icao4 not in goals_icao and icao4 != self.location.icao:
                goals_icao.append(icao4)
                self.goals[icao4] = object4
                print(len(goals_icao))
                print(self.goals)
        print("Asetetaan tavoitteet:")
        for icao in goals_icao:
            self.airports[icao].goal = True
            print(self.airports[icao].name)

    def fly(self, flight_type, dest): #Ottaa pelaajan syötteet ja tekee muutokset attribuutteihin.
        dist = int(distance.distance((self.location.lat, self.location.lon), (self.airports[dest].lat, self.airports[dest].lon)).km)
        if flight_type == "SMALL":
            cost = int(dist*0.3)
            co2 = int(dist*0.1)
        elif flight_type == "NORMAL":
            cost = int(dist*0.2)
            co2 = int(dist*0.2)
        elif flight_type == "HIGH":
            cost = int(dist*0.1)
            co2 = int(dist*0.3)
        else:
            cost = dist  #oletuskerroin on 1
            co2 = dist   #oletuskerroin on 1

        self.flights_total = self.flights_total + 1
        self.money = self.money - cost
        self.money_spent_total = self.money_spent_total + cost
        self.co2 = self.co2 + co2
        self.location = self.airports[dest]
        self.message = f"Saavut lentokentälle {self.location.name}"
        self.flights = self.location.flights
        print(f"Saavut lentokentälle {self.location.name}. ")

        if dest in self.goals and self.goals[dest].visited == False:
            #self.goals[dest].visited = True ## Tämä on sama objekti kuin airports[dest]!!
            self.message = self.message + f"Saavutit tavoitteen {self.goals[dest].name}. "
            print(f"Saavutit tavoitteen {self.goals[dest].name}")

        if self.airports[dest].visited == False:
            self.airports[dest].visited = True
            gain = int(self.airports[dest].gdp * 2 ) # Rahaa saa 2*gdp. Arvon muuttaminen vaikuttaa vaikeusasteeseen.
            self.money = self.money + gain
            self.money_gained = gain
            self.money_gained_total = self.money_gained_total +gain
            print(f"Saavut lentokentälle {self.location.name}, saat rahaa {gain}")
            self.message = self.message +f"Saavut lentokentälle {self.location.name}, saat rahaa {gain}. "

    def bonus_flights(self): #Luo (yhden) satunnaisen lennon
        old_dest = []
        for flight in self.flights:
            old_dest.append(flight["icao"])
        print("Normaalit lennot pelaajan sijainnissa:",old_dest)
        random_icao = random.choice(list(self.airports.values())).icao
        if random_icao not in old_dest:
            new_dest = self.airports[random_icao]
            dist = int(distance.distance((self.location.lat, self.location.lon), (new_dest.lat, new_dest.lon)).km)
            cost = dist
            co2 = dist
            flight = {"name": new_dest.name, "country": new_dest.country, "icao": new_dest.icao, "cost": cost, "distance": dist,
                      "co2": co2, "lat": new_dest.lat, "lon": new_dest.lon, "bonus_flight": True }
            self.flights.append(flight)
            print("Jokerilento:",flight)

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

    def save_game(self): #Tallentaa pelin tiedot tietokantaan

        if self.id == "default": #jos peliä ei vielä syötetty:
            newgame_sql = (f"INSERT INTO game(name, location, money, co2, money_gained, money_spent, distance, flights, difficulty,start_money,status) "
                        f"VALUES( '{self.name}','{self.location.icao}','{self.money}','{self.co2}','{self.money_gained_total}','{self.money_spent_total}','{self.distance}','{self.flights_total}','{self.difficulty}','{self.start_money}','{self.game_status}')")
            print(newgame_sql)
            kursori.execute(newgame_sql)
            yhteys.commit()
            id_sql = f"SELECT id FROM game WHERE name = '{self.name}'"
            kursori.execute(id_sql)
            self.id = kursori.fetchall()[0][0]
            print("tallennetun pelin id:")
            print(self.id)
            print("tallennetaan tavoitteet", self.goals )

            for goal in self.goals.values():
                goal_sql = f"INSERT INTO goal(game_id,ident,reached) VALUES ('{self.id}','{goal.icao}', '0' )"
                print(goal_sql)
                kursori.execute(goal_sql)
            yhteys.commit()

            #Pelaajan aloituskenttä merkitään käydyksi:
            for airport in self.airports.values():
                if airport.visited == True:
                    visited_sql = f"INSERT INTO visited(game_id, ident) VALUES ('{self.id}','{airport.icao}');"
                    print(visited_sql)
                    kursori.execute(visited_sql)
                    airport.db_saved = True
            yhteys.commit()

        else: #Jos peli on jo syötetty
            save_sql = (f"UPDATE game "
                   f"SET game.location = '{self.location.icao}', game.money = '{self.money}', game.co2 = '{self.co2}' , game.money_gained = '{self.money_gained_total}', game.money_spent = '{self.money_spent_total}', "
                   f"game.distance = '{self.distance}', game.flights = '{self.flights_total}', game.difficulty = '{self.difficulty}', game.start_money = '{self.start_money}', game.status = '{self.game_status}'"
                   f" WHERE game.id ='{self.id}'")
            print(save_sql)
            kursori.execute(save_sql)
            yhteys.commit()

            #visited_sql
            db_visited_list = []
            get_visited_sql = f"SELECT ident FROM visited WHERE game_id = '{self.id}'"
            kursori.execute(get_visited_sql)
            db_visited = kursori.fetchall()
            for ident in db_visited:
                db_visited_list.append(ident[0])
                print("Käyty kentällä:", ident[0])

            for airport in self.airports.values():
                if airport.visited == True and airport.icao not in db_visited_list:
                    visited_sql = f"INSERT INTO visited(game_id, ident) VALUES ('{self.id}','{airport.icao}');"
                    print(visited_sql)
                    kursori.execute(visited_sql)
                    airport.db_saved = True
            yhteys.commit()

            #goal_sql
            for goal in self.goals.values():
                if goal.visited == True:  # vanha: INSERT INTO goal(game_id,ident,reached) VALUES '{self.id}','{goal.values().icao}', '1' ON DUPLICATE KEY
                    goal_sql = f"UPDATE goal SET goal.reached = '1' WHERE goal.game_id = '{self.id}' AND goal.ident = '{goal.icao}' ;"
                    print(goal_sql)
                    kursori.execute(goal_sql)
            yhteys.commit()


##################################################################################################################
## Airport luokka
class Airport:
    airports = {}

    def __init__(self, game, **kwargs):         #Ottaa game objektin ja tietokannan attribuutit
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.flights = []                       #Annetaan lentolista attr
        game.airports[self.icao] = self         #Laittaa airport objektin game objektin airports dictiin



    def create_flights(self, game): #Luo 3 lentoa lentokentältä.
        flights_all = [] #Tehdään lennot kaikille muille kentille
        for key, object in game.airports.items():
            if object != self:
                dist = int(distance.distance((self.lat, self.lon), (object.lat, object.lon)).km)
                cost = dist #OLETUSKERROIN TÄHÄN JOS HALUTAAN VÄHÄPÄÄSTOISEN LENNON KERROIN = 0.3, HALVIN = 0.1
                co2 = dist #OLETUSKERROIN TÄHÄN JOS HALUTAAN VÄHÄPÄÄSTOISEN LENNON KERROIN = 0.1
                flight =  {"name": object.name, "country": object.country, "icao": object.icao, "cost": cost, "distance": dist, "co2": co2,"lat": object.lat, "lon": object.lon, "bonus_flight":False}
                flights_all.append(flight)
                #print(flight)
        #Järjestetään lennot etäisyyden mukaan ja syötetään 3 lähintä:
        flights_all = sorted(flights_all, key=lambda flight: flight["distance"])
        for n in range (0,3):
            self.flights.append(flights_all[n])

    def return_flights(self, game): #Luo paluulentoja lentokentiltä joilla ei plauuyhteyttä.
        for dest in self.flights:                       #Jokaista määränpäätä kohden.
            #print(dest["icao"]),print(dest["name"])
            return_flight_exists = False
            for dest_flight in game.airports[dest["icao"]].flights: #Jos määränpään lentolistassa on paluulento...
                if dest_flight["icao"] == self.icao:
                    return_flight_exists = True

            if return_flight_exists == False: #Luodaan paluulento create_1_flight metodilla:
                game.airports[dest["icao"]].create_1_flight(self)

    def create_1_flight(self, object): #Luo self-objektille lennon argumentin objektiin.
        dist = int(distance.distance((self.lat, self.lon), (object.lat, object.lon)).km)
        cost = dist
        co2 = dist
        flight = {"name": object.name, "country": object.country, "icao": object.icao, "cost": cost, "distance": dist,"co2": co2, "lat": object.lat, "lon": object.lon,"bonus_flight":False}
        self.flights.append(flight)
        # print(flight)

##################################################################################################################
## Tietorakenne ##
#Game objektin attribuuttien oletusarvot:
game_data_default = {
        "id":"default",
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
        "flights_total": 0,
        "distance": 0,
        "location": object,
        "flights": [],
        "airports": {},
        "goals": {}
}

#Lentokentän ja lennon tietorakenne:
#airport_default = {"goal": False, "visited": False, "icao": "efhk", "name": "vantaa", "country": "suomi", "lat": "50.22","lon": "20.22", "gdp": "10", "db_saved": False}
#flight_default = {"name": "a", "country": "suomi", "icao": "efhk", "cost": "x", "distance": "100", "co2": "50","lat": "50.22", "lon": "20.22"}

##################################################################################################################
## Pääohjelma ##

## Tietokanta
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',"collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

## Funktiot

## Pääohjelman koodi:
#Pääohjelma hakee tietokannasta tallennetut pelit ja syöttää ne olioina Game-luokkaan
# ensin luodaan objektit oletustiedoilla, sitten muokataan attr tietokannan mukaan

kursori2 = yhteys.cursor(dictionary=True)
game_sql = f"SELECT * FROM game"
kursori2.execute(game_sql)
game_vastaus = kursori2.fetchall()
for rivi in game_vastaus:
    loaded_game = Game(**game_data_default) #Luokkaan oletus attr

    loaded_game.game_status = rivi["status"]
    loaded_game.message = rivi["message"]
    loaded_game.debugmessage = rivi["debugmessage"]
    loaded_game.name= rivi["name"]
    loaded_game.difficulty = rivi["difficulty"]
    loaded_game.location = loaded_game.airports[rivi["location"]]
    loaded_game.money = rivi["money"]
    loaded_game.money_gained_total = rivi["money_gained"]
    loaded_game.co2 = rivi["co2"]
    loaded_game.money_spent_total = rivi["money_spent"]
    loaded_game.flights_total = rivi["flights"]
    loaded_game.distance = rivi["distance"]
    loaded_game.start_money = rivi["start_money"]
    loaded_game.flights = loaded_game.location.flights
    Game.games[loaded_game.name] = loaded_game  # lisätään Game.games dictiin

    loaded_game_id = rivi["id"] #id tarvitaan seuraavaan sql hakuun
    goal_sql = f"SELECT * FROM goal WHERE game_id={loaded_game_id}" #Haetaan tavoitteet
    kursori2.execute(goal_sql)
    goal_vastaus = kursori2.fetchall()
    for rivi in goal_vastaus:
        loaded_game.goals[rivi["ident"]] = loaded_game.airports[rivi["ident"]] #Laitetaan airport obj goals dict
        loaded_game.goals[rivi["ident"]].goal = True    #Laitetaan airport obj goal attr = True

    visited_sql = f"SELECT * FROM visited WHERE game_id={loaded_game_id}"
    kursori2.execute(visited_sql)
    visited_vastaus = kursori2.fetchall()
    for rivi in visited_vastaus:
        loaded_game.airports[rivi["ident"]].visited = True #Airport visited attr = True kaikille vierailluille kentille
    print("Haetaan tallennetut pelit:")
    print(loaded_game.name, Game.games[loaded_game.name])


##################################################################################################################
## Flask ##
# Flask serveri pitää olla viimeisenä koodissa jotta muuttujat ja funktiot on määritelty.
app = Flask(__name__)
CORS(app)

@app.route('/loadgame/<name>')
def server_loadgame(name): #Vaihtaa aktiivisen peliobjektin nimen perusteella
    Game.active_game = name
    return json.dumps(Game.games[Game.active_game].get_data())

@app.route('/newgame/<nimi>/<difficulty>')
def server_newgame(nimi, difficulty): #Alustaa uuden Game-luokan objektin ja palauttaa pelin tilanteen.
    new_game = Game(**game_data_default)                            #Määritellään pelaaja Game luokkaan oletus attribuuteilla
    Game.games[nimi] = new_game                                     #Pelaajaoliota kutsutaan: Game.games[active_game] Olisi parempi laittaa vain Game.active_game...
    Game.active_game = nimi                                         #Laitetaan luokkamuuttuja osoittamaan uusimpaan peliin
    Game.games[Game.active_game].name = nimi
    Game.games[Game.active_game].set_difficulty(difficulty)         #Asettaa aloitusrahat ja vaikeusasteen
    Game.games[Game.active_game].start_and_goals()                  #Antaa pelaajalle sijainnin ja tavoitteet ja lennot
    Game.games[Game.active_game].bonus_flights()                    #Antaa pelaajalla ylimääräisen lennon jonnekin
    print("Uuden pelin tavoitteet:", Game.games[Game.active_game].goals)
    print("Kaikki pelit games-listassa:", Game.games)
    #Game.games[Game.active_game].save_game()                       #Tallentaa tietokantaan. Poistetaan käytöstä newgamessa toistaiseksi
    return json.dumps(Game.games[Game.active_game].get_data())      #haetaan pelin tilanne game.get_data()


@app.route('/<flight_type>/<destination>')
def server_input(flight_type, destination):
    destination = destination.upper()                                #ICAO koodit on isolla kirjaimella
    flight_type = flight_type.upper()                                #Lentoluokka SMALL/NORMAL/HIGH
    Game.games[Game.active_game].fly(flight_type, destination)       #tekee lennon muutokset (lisää päästöjä, vähemmän rahaa, saapumispalkkio, )
    Game.games[Game.active_game].bonus_flights()                     #Lisätään lentoja pelaajan lentolistaan
    Game.games[Game.active_game].goal_check()                        #TArkistaa onko pelaaja voittanut pelin. Palauttaa gamewon tai gameinprogress
    Game.games[Game.active_game].money_check()                       #Tarkistaa voiko pelaaja enää lentää. Palauttaa gameover tai gameinprogress kunhan peliä ei ole voitettu.
    Game.games[Game.active_game].save_game()                         #Tallentaa tietokantaan
    return json.dumps(Game.games[Game.active_game].get_data())       #haetaan pelin tilanne game.get_data()


@app.route('/gamelist')
def server_gamelist(): #Palauttaa listan Game luokan objektien tiedoista. Avain on pelaajan nimi. #Muutetaan ARRAYKSI!!
    gamelist = []
    for key, object in Game.games.items():
        gamelist.append(object.get_data())
    return json.dumps(gamelist)

if True:
    app.run(host='127.0.0.1', port=3000) # use_reloader=True pois toistaiseksi


