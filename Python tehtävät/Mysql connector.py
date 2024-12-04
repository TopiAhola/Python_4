import mysql.connector

# Piti ladata mysql_connector mysql_connector_python ei toiminut....

# Tehdää sanakirja. Sanakirjan voi laittaa syötteeksi mysql.connectoriin jos siihen lisää **
# ** muuttaaa avain:arvo parit nimetyiksi argumenteiksi jotka annetaan funktiolle.
# eli def funktio( a, b ) saa argumetit (100, 200) jos sanakirjassa ( a:100 , b:200)
# Jee!


parametrit = {
    "host" :'localhost',
    'database' :'ankkalinna',
    'user' : 'topi',
    'password' : ''
            }

yhteys = mysql.connector.connect(**parametrit)

sql = f"SELECT etunimi FROM ankkalinnalainen where sukunimi ='ankka'"
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()
print(tulos)

# Toimii!!!







