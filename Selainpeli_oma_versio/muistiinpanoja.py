#Lentokenttä tietorakenne:
location = {"goal": True , "visited": True, "icao":"efhk", "name": "helsinki", "country": "suomi", "lat": "50.22", "lon": "20.22", "gdp": "0" }
+lisättävä lentokentän rahabonus?


#Lentoreititn oliorakenne?:



#game_data tietorakenne:
game_data = {
        "game_status": "gameinprogress/gameover/game won",
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
#game_data loppu


