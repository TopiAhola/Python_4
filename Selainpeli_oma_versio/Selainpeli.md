## Eurooppalainen Turisti - Selainpeli

### Sivu - HTML, CSS ja JavaSCript
Sivu sisältää käyttöliittymän joka näyttää pelin tilanteen palvelimen palauttaman json-objektin perusteella. <br>
Sivulla on nappuloita joita klikkaamalla pelaaja valitsee lennon.
<br>
### Palvelin - Python
Palvelin ottaa vastaan pelaajan syötteen ja palauttaa pelin tilanteen json-objektina.<br>
Python koodi käyttää luokkia ja olioita. 

### Tietokanta - MariaDB
Tietokantayhteyden nimi on "yhteys": <br>
yhteys = mysql.connector.connect(**parametrit) 

Kursorin nimi on "kursori": <br>
kursori = yhteys.cursor()

Tietokantaa käytetään käyttäjällä "game" <br>
parametrit = 
{"host" :'localhost', 
'database' :'flight_game', 
'user' : 'game',
'password' : '', 
"collation" : "latin1_swedish_ci"}


<img src="https://github.com/user-attachments/assets/8e5a8ea8-b712-43ff-a5bd-ad7815cd692a" width="75%" height="75%">



#### Python importit
import mysql.connector <br>
import random <br>
from geopy import distance <br>
import json

#### Python funktiot
Funktiot tehdään uusiksi

