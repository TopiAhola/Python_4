
# Importit
import mysql.connector
import random
from geopy import distance


# Yhteys tietokantaan
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',
              "collation": "latin1_swedish_ci"}

yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

def game_values(game_id):
    #Ottaa game:id ja palauttaa game taulun tiedot listana.

    values = []

    sql = f"SELECT * FROM game WHERE game.id = '{game_id}';"
    kursori.execute(sql)
    sql_list = kursori.fetchall()

    for tuple in sql_list:
        for n in range(0, 9):
            values.append(tuple[n])

    #Palautetaan lista
    return values





###########################################

game_id = 43
game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights = game_values(game_id)

game_id = 43


sql3 = f"SELECT money_gained FROM game WHERE game.id = '{game_id}' "
kursori.execute(sql3)
sql_gained = kursori.fetchall()
gained = sql_gained[0][0]
money_gained = int(gained +gdp_bonus)
print(gained)


#sql_read = kursori.fetchall()
#print(sql_read)


#yhteys.commit()

