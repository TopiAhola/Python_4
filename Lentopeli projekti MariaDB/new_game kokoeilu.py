# Importit
import mysql.connector
import random
from geopy import distance

# Yhteys tietokantaan
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',
              "collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()



def random_location():
    #Antaa satunnaisen kentan ident-koodin

    #Haetaan kenttien ident.koodit listaan:
    sql = f"SELECT ident FROM kentat;"
    kursori.execute(sql)
    list = kursori.fetchall()


    #Arvotaan kenttä väliltä 0, listan pituus-1
    n = random.randint(0, len(list)-1)

    #Karsitaan erikoimerkit pois listaobjektista
    location = str(list[n])
    location = location.replace("('", "")
    location = location.replace("',)", "")

    #Palautetaan ident-koodi
    return location



def new_game():
    # Luo pelaajan ja tavoitteet ja syöttää ne tietokantaan.
    # Palauttaa pelaajan game_id tietokannasta.
    # Palauttaa tavoitteet listana goal_list



    name = input("Pelaajan nimi: ")
    location = random_location()
    money = 1500
    co2 = 0
    money_gained = 0
    money_spent = 0
    distance = 0
    flights = 0

    sql_game = (f"INSERT INTO game(name, location, money, co2, money_gained, money_spent, distance, flights) "
            f"VALUES ('{name}', '{location}', '{money}', '{co2}', '{money_gained}', '{money_spent}', '{distance}', '{flights}' )")
    kursori.execute(sql_game)
    yhteys.commit()


    #Haetaan uusimman pelin id:
    sql2 = f"SELECT id FROM game WHERE id IN (SELECT max(id) FROM game)"
    kursori.execute(sql2)
    sql_tuple = kursori.fetchone()
    #kursori.close()
    game_id =sql_tuple[0]

    # Arvotaan tavoitteet
    goal_list = []
    while len(goal_list) < 5:
        kentta = random_location()
        if kentta != location and kentta not in goal_list:
            goal_list.append(kentta)

    for kentta in goal_list:
        sql_goal = (f"INSERT INTO goal(game_id, ident, reached)"
                    f"VALUES('{game_id}', '{kentta}', '0')   ")
        kursori.execute(sql_goal)
        yhteys.commit()






    return game_id, name, location, money, co2, money_gained, money_spent, distance, flights, goal_list

#pääohjelma

game_id, goal_list = new_game()
print(game_id)
print("testi")
print(goal_list)