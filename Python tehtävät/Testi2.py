import mysql.connector

def sql_request(icao):


    parametrit = {
        "host": 'localhost',
        'database': 'flight_game',
        'user': 'topi',
        'password': ''}
    yhteys = mysql.connector.connect(**parametrit)
    cursor = yhteys.cursor()

    #sql = f"SELECT name, municipality from airport where ident = '{icao}'  "
    #cursor.execute(sql)
    # tulos = cursor.fetchall()

    nimi = "a"
    kaupunki= "b"

    return nimi, kaupunki

nimi, kaupunki = sql_request("aaaa")
print(nimi)
print(kaupunki)