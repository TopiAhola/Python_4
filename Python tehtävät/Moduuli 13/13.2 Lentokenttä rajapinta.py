'''
Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan
muodossa: http://127.0.0.1:3000/kenttä/EFHK.
Vastauksen on oltava muodossa:
{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.


'''

from flask import Flask, request
import mysql.connector


app = Flask(__name__)
@app.route('/kentta/<icao>')

def kentta(icao):
    icao = icao.upper()
    nimi, kaupunki = sql_request(icao)

    vastaus = {"ICAO" : icao,
               "Name" : nimi,
               "Municipality" : kaupunki
               }

    return vastaus

def sql_request(icao):


    parametrit = {
        "host": 'localhost',
        'database': 'flight_game',
        'user': 'topi',
        'password': ''}
    yhteys = mysql.connector.connect(**parametrit)
    cursor = yhteys.cursor()

    #sql = f"SELECT name, municipality from airport where ident = '{icao}'  "
    sql = f"SELECT name, municipality from kentat where ident = '{icao}' "
    cursor.execute(sql)
    tulos = cursor.fetchall()

    nimi = tulos[0][0]
    kaupunki= tulos[0][1]

    return nimi, kaupunki

#Pääohjelma
# if True näyttää toimivan myös... Miksi tämä on kirjoitettu näin?
# __name__ == __main__ kun script ajetaan suoraan eikä osana pakettia?
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

