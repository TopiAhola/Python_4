'''
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava
GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
'''

import requests
from flask import Flask
from flask import request

'''
luku = input("Anna luku: ")
pyynto = f"http://127.0.0.1:3000/alkuluku?{luku} "
vastaus = requests.get(pyynto).json()
print(vastaus)
'''
# Tämä toimii: !
#http://127.0.0.1:3000/alkuluku?luku=5

app = Flask(__name__)
@app.route('/alkuluku/<luku>')

def alkuluku(luku):

    #Tämä oli tapa hakea luku jos oli osoitteessa ?-jälkeen
    #args = request.args
    #luku = int(args.get("luku"))

    #Osoite on string, mutta luvun pitää olla int
    luku = int(luku)
    #Pyydetään totuusarvo funktiosta:
    bool_value = alkuluku_tarkista(luku)

    #Muotoillaan vastaus:
    vastaus = {"number" : luku,
               "isPrime" : bool_value
               }

    return vastaus

def alkuluku_tarkista(luku):
#Ottaa luvun ja palauttaa bool_value True tai False
    n = 2
    while n<luku:
        #Jos jakojäännös on 0, luku on jaollinen muuttujalla n.
        if luku % n == 0:
            #print(f"On jaollinen luvulla {n}")
            #print(f" {luku} / {n} = {luku/n}")
            #print("Luku ei ole alkuluku")
            bool_value = False
            break

        #Jos jakojäännös ei ole 0 lisätään muuttujan n arvoa yhdellä.
        else:
            #print(f"Kokeiltu jakaa: {n}")
            n = n + 1

    else:
        #print(f"Luku {luku} on alkuluku!")
        bool_value = True

    return bool_value


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

# Syöte selaimeen: http://127.0.0.1:3000/alkuluku/11
# Palauttaa vastauksen muodossa: {'number': 11, 'isPrime': True}