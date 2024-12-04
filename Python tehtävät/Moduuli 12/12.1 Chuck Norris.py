'''
Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
Käyttäjälle on näytettävä pelkkä vitsin teksti.


'''
from msvcrt import getch

import requests

pyynto = "https://api.chucknorris.io/jokes/random"

#Palauttaa sanakirjan
vastaus = requests.get(pyynto).json()

#Tulostetaan vitsin teksti "value"
tuloste = vastaus["value"]
print(f"\n{tuloste}\n ")

