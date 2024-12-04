def end_game(game_id):
#Pelaaja voittaa pelin. Tulostetaan lopputiedot.
    game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights = game_values(game_id)
    co2_kg_km = game_co2 /game_distance

    print(f"Onnea {game_name}! Olet saavuttanut tavoitteesi.")
    print(f"\nTavoitteesi olivat:")
    goal_list = goal_reach_list(game_id)
    for tuple in goal_list:
        print(f"{tuple[0]}, {tuple[1]}")


    print(f"Lensit {game_flights} kertaa lentokoneella. Matkustit yhteensä {game_distance}km. \n"
          f"Päästösi yhteensä olivat {game_co2}. Päästösi kilometriä kohden olivat {co2_kg_km}kg/km. \n"
          f"  ")

    print(f"Ansaitsit {game_money_gained}€. Kulutit {game_money_spent}€. Sinulle jäi {game_money}€ rahaa.")




def get_money(game_id, game_location):
# Antaa pelaajalle lisää rahaa. Voisi myös tulostaa jonkin selityksen mistä raha tulee.

    #Haetaan pelaajan rahat
    sql = f"SELECT money FROM game WHERE game.id = '{game_id}' "
    kursori.execute(sql)
    sql_money = kursori.fetchall()

    #Haetaan maan GDP
    sql = f"SELECT gdp FROM kentat WHERE kentat.ident = '{game_location}' "
    kursori.execute(sql)
    sql_gdp = kursori.fetchall()

    #Rahaa saa 2*gdp. Arvon muuttaminen vaikuttaa vaikeusasteeseen.
    gdp = sql_gdp[0][0]
    gdp_bonus = int(3 * gdp)
    money1 = sql_money[0][0]
    money2 = int(money1 +gdp_bonus)
    print(f"Ansaitset {gdp_bonus}€ lisää rahaa.")

    sql2 = f"UPDATE game SET money = '{money2}' WHERE game.id = '{game_id}'"
    kursori.execute(sql2)
    yhteys.commit()



def visit_destination(game_location, game_id):
#Tarkistaa onko pelaaja käynyt kohteessa. Muokkaa tietokantaan käydyt kentät.

    #Tarkistetaan onko kentta tavoite:
    sql1 = f" SELECT * from goal WHERE game_id = '{game_id}'  "
    kursori.execute(sql1)
    goal_list = kursori.fetchall()
    #print(goal_list)

    #Käydään tuplet läpi ja jos löytyy tavoite jossa reached == 0 merkitään se saavutetuksi.
    for tuple in goal_list:
        #print(tuple[2])
        if game_location in tuple and tuple[2] == 0:
            print(f"\nOlet saavuttanut yhden tavoitteistasi!")
            sql2 = f"UPDATE goal SET reached = '1' WHERE game_id = '{game_id}' and ident = '{game_location}'  "
            kursori.execute(sql2)
            yhteys.commit()

    #Tarkistetaan onko kentällä käyty aikaisemmin

    sql3 = f" SELECT ident FROM visited WHERE game_id = '{game_id}'  "
    kursori.execute(sql3)
    sql_list = kursori.fetchall()
    visited_list = []
    for tuple in sql_list:
        #print(tuple[0])
        visited_list.append(tuple[0])


    if game_location not in visited_list:
        print("Vierailet ensimmäistä kertaa tässä maassa.")
        sql4 = f"INSERT INTO visited (game_id, ident) VALUES ('{game_id}', '{game_location}') "
        kursori.execute(sql4)
        yhteys.commit()
        get_money(game_id, game_location)
    else:
        print("Olet käynyt tässä maassa aikaisemmin.")




def update_game(game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights):
# Tallentaa muutoksia game-tauluun
    sql = (f"UPDATE game "
           f"SET game.location = '{game_location}', game.money = '{game_money}', game.co2 = '{game_co2}' , game.money_gained = '{game_money_gained}', game.money_spent = '{game_money_spent}', "
           f"game.distance = '{game_distance}', game.flights = '{game_flights}' WHERE game.id = '{game_id}' ")

    kursori.execute(sql)
    yhteys.commit()



def fly(selected_flight, game_id):
# Ottaa lennon tiedot. Hakee pelin tiedot ja muokkaa niitä lennon mukaisesti.
# selected_flight =(destination, name, country, distance, cost, co2)


    game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights = game_values(game_id)

    game_location = selected_flight[0]
    game_distance = game_distance + selected_flight[3]
    game_money = game_money - selected_flight[4]
    game_co2 = game_co2 + selected_flight[5]
    game_money_spent = game_money_spent + selected_flight[4]
    game_distance = game_distance + selected_flight[3]
    game_flights = game_flights + 1

    update_game(game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights)


def select_flight(flights):
    print(f"\nTarjolla on seuraavat lennot: ")
    n = 1
    print("\nVähäpäästöiset lennot: ")
    for tuple in flights[0:4]:
        print(f"{n}: {tuple[1]}, {tuple[2]}, etäisyys {tuple[3]}km, hinta {tuple[4]}€, päästöt {tuple[5]}kg")
        n = n + 1
    print("\nKeskipäästöiset lennot: ")
    for tuple in flights[4:8]:
        print(f"{n}: {tuple[1]}, {tuple[2]}, etäisyys {tuple[3]}km, hinta {tuple[4]}€, päästöt {tuple[5]}kg")
        n = n + 1
    print("\nSuuripäästöiset lennot: ")
    for tuple in flights[8:12]:
        print(f"{n}: {tuple[1]}, {tuple[2]}, etäisyys {tuple[3]}km, hinta {tuple[4]}€, päästöt {tuple[5]}kg")
        n = n + 1

    selection = int(input("\nValitse lento 1-12:\n"))
    selected_flight = flights[selection - 1]
    return selected_flight


def get_flights(game_location, kentta1, kentta2, kentta3, kentta4):
    # Palauttaa 3 listaa tupleja lennoista jotka ovat tarjolla.
    # tuple =(id, destination, distance, cost, co2)
    # vähäpäästöinen luokka on flights[0]-[3]

    flights = []

    kentat = [kentta1, kentta2, kentta3, kentta4]


    #Luokka 1, vähäpäästöinen

    for dest in kentat:
        dis = int(dist(game_location, dest))
        co2 = int(0.1 * dist(game_location, dest))
        cost = int(0.3 * dist(game_location, dest))
        name, country = get_name_country(dest)
        tuple = (dest, name, country, dis, cost, co2)
        flights.append(tuple)


    # Luokka 2, keskipäästöinen

    for dest in kentat:
        dis = int(dist(game_location, dest))
        co2 = int(0.2 * dist(game_location, dest))
        cost = int(0.2 * dist(game_location, dest))
        name, country = get_name_country(dest)
        tuple = (dest, name, country, dis, cost, co2)
        flights.append(tuple)




    # Luokka 3, suuripäästöinen

    for dest in kentat:
        dis = int(dist(game_location, dest))
        co2 = int(0.3 * dist(game_location, dest))
        cost = int(0.1 * dist(game_location, dest))
        name, country = get_name_country(dest)
        tuple = (dest, name, country, dis, cost, co2)
        flights.append(tuple)


    return flights



def get_destinations(game_location):
#Ottaa sijainnin ja antaa vaihtoehdot minne lentää.

    # 3 lähintä kenttää. Tupleja (ident, distance)
    nearby = get_nearby(game_location)
    kentta1, kentta2, kentta3 = nearby

    #identit kentille:
    kentta1_ident = kentta1[0]
    kentta2_ident = kentta2[0]
    kentta3_ident = kentta3[0]
    kentta4_ident = (get_jokeri(game_location, kentta1[0], kentta2[0], kentta3[0]))

    return kentta1_ident, kentta2_ident, kentta3_ident, kentta4_ident


def get_jokeri(game_location, nearest1, nearest2, nearest3):
#Ottaa pelaajan sijainnin ja antaa sattumanvaraisen matkakohteen identin.
# Argumentit on game_location ja 3 kenttää jotka get_destinations arpoo. Ei anna samaa kenttää uudestaan.
    while True:
        jokeri_ident = random_location()
        if jokeri_ident != game_location and jokeri_ident != nearest1 and jokeri_ident != nearest2 and jokeri_ident != nearest3:
            break

    return jokeri_ident



def check_money(game_money, kentta1_dist, kentta2_dist, kentta3_dist, kentta4_dist):
    # Tarkistaa onko pelaajalla rahaa lentää kentille halvimmalla lipulla.
    # Tämä on yksinkertainen versio. Parempi antaa pelaajan statsit ja ei tee pyöristysvirheitä.
    kentta1_cost = 0.1 * kentta1_dist
    kentta2_cost = 0.1 * kentta2_dist
    kentta3_cost = 0.1 * kentta3_dist
    kentta4_cost = 0.1 * kentta4_dist
    costs = [kentta1_cost, kentta2_cost, kentta3_cost, kentta4_cost]
    min_cost = min(costs)


    if game_money < min_cost:
        print(f"\nRahasi ovat loppuneet ja olet hävinnyt pelin!\n")
        exit()

def get_name_country(ident):
    #hakee kentän nimen identin perusteella. Tämä on vähän turha.

    sql = f"SELECT name, country_fi FROM kentat WHERE ident = '{ident}'  "
    kursori.execute(sql)
    sql_read = kursori.fetchall()
    for a in sql_read:
        name = a[0]
        country_fi = a[1]
    return name, country_fi



def get_nearby(game_location):
# Ottaa pelaajan sijainnin ja palauttaa 3:n lähimmän kentän identin ja etäisyyden .

    #Haetaan lista kaikista kentistä, all_kentat
    sql = f"SELECT ident FROM kentat"
    kursori.execute(sql)
    sql_list = kursori.fetchall()
    all_kentat = []
    for rivi in sql_list:
        all_kentat.append(rivi[0])

    #Lasketaan etäisyys kaikille kentille, tehdään kentistä ja etäisyyksistä tupleja.
    all_dist = []

    for kentta in all_kentat:
        if kentta != game_location:
            #print(kentta, game_location)
            kentta_dist = dist(kentta, game_location)
            kentta_tuple = (kentta, kentta_dist)
            all_dist.append(kentta_tuple)

    # Järjestellään tuplet pienimmät ensin
    all_dist = sorted(all_dist, key=lambda x: x[1])

    #Lähimmät 3 kenttää tupleina
    nearby = []
    nearby = all_dist[:3]

    return nearby


def dist( origin, destination ):
# Laskee kahden kentän välisen etäisyyden. Syöte on kenttien ident-koodi. Antaa tuloksen kilometreinä kokonaislukuna.

     #Haetaan koordinaatit
    sql1= f"select longitude_deg, latitude_deg from kentat where ident ='{origin}'  "
    sql2= f"select longitude_deg, latitude_deg from kentat where ident ='{destination}' "

    kursori.execute(sql1)
    tulos1 = kursori.fetchall()
    kursori.execute(sql2)
    tulos2 = kursori.fetchall()
    #kursori.close()

    #lasketaan etäisyys, muunnetaan kokonaisluvuksi
    dist = int(distance.distance(tulos1, tulos2).km)

    return dist


def random_location():
    #Antaa satunnaisen kentan ident-koodin

    #Haetaan kenttien ident.koodit listaan:
    sql = f"SELECT ident FROM kentat;"
    kursori.execute(sql)
    list = kursori.fetchall()
    #kursori.close()

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


    return game_id

def load_game():
    #Näyttää edelliset pelit ja antaa pelaajan valita game_id numeron

    sql = f"SELECT game.id, game.name, kentat.name, kentat.country_fi FROM game LEFT JOIN kentat ON kentat.ident = game.location"
    kursori.execute(sql)
    sql_list = kursori.fetchall()

    print("\nTallennetut pelit:\nNumero, Nimi, Lentokenttä, Maa")
    for game in sql_list:
        print(f"{game[0]}, {game[1]}, {game[2]}, {game[3]}")

    game_id = input("Anna haluamasi pelin numero: ")
    if game_id == "":
        game_id = new_game()


    return game_id


def goal_reached(game_id):
    #Hakee saavutettujen tavoitteiden totuusarvot tietokannasta.
    #Palauttaa True jos kaikki arvot != 0
    goal_bool = False


    sql = f"SELECT reached FROM goal WHERE game_id = '{game_id}';"
    kursori.execute(sql)
    sql_list = kursori.fetchall()

    #Muutetaan SQL tuplet 0 tai 1 arvoksi
    bool_values = []
    for rivi in sql_list:
        bool_values.append(rivi[0])

    if 0 not in bool_values:
        goal_bool = True


    return goal_bool

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

def goal_reached(game_id):

    # Kertoo pelaajan saavutetut tavoitteet.

    sql = f" SELECT kentat.name, kentat.country_fi FROM kentat RIGHT JOIN goal ON goal.ident = kentat.ident WHERE goal.game_id = '{game_id}' AND goal.reached = '1' "
    kursori.execute(sql)
    sql_list = kursori.fetchall()
    goal_list = []
    for tuple in sql_list:
        goal_list.append(tuple)

    return goal_list



def show_goals(game_id):
    #Kertoo pelaajan tavoitteet ja missä on käynyt.

    sql = f" SELECT kentat.name, kentat.country_fi FROM kentat RIGHT JOIN goal ON goal.ident = kentat.ident WHERE goal.game_id = '{game_id}' AND goal.reached = '0' "
    kursori.execute(sql)
    sql_list = kursori.fetchall()
    goal_list = []
    for tuple in sql_list:
        goal_list.append(tuple)

    print(f"\nSinulla on {len(goal_list)} tavoitetta jäljellä: \n")
    for tuple in goal_list:
        print(f"{tuple[0]}, {tuple[1]}")

def show_location(game_id):
    #Kertoo pelaajan sijainnin. Lentokenttä ja maa.

    sql = f" SELECT kentat.name, kentat.country_fi FROM kentat RIGHT JOIN game ON game.location = kentat.ident WHERE game.id = '{game_id}'  "
    kursori.execute(sql)
    sql_list = kursori.fetchall()

    location = ()
    for tuple in sql_list:
        location += tuple
        print(f"\nSijaintisi on {location[0]}, {location[1]}")



## PÄÄOHJELMA

# Importit
import mysql.connector
import random
from geopy import distance

# Yhteys tietokantaan
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',
              "collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

#########################################################################3




game_id = 41
game_location = "EVRA"
game_money = 100
kentta1 = "UMMS"
kentta2 = "EETN"
kentta3 = "LMML"
kentta4 = "LATI"

flights = get_flights(game_location, kentta1, kentta2, kentta3, kentta4)

selected_flight = select_flight(flights)
print(selected_flight)

fly(selected_flight, game_id)

game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights = game_values(game_id)

visit_destination(game_location, game_id)

end_game(game_id)




