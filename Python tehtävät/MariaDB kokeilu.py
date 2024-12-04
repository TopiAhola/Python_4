import mariadb

# Tehdää sanakirja. Sanakirjan voi laittaa syötteeksi mysql.connectoriin jos siihen lisää **
# ** muuttaaa avain:arvo parit nimetyiksi argumenteiksi jotka annetaan funktiolle.
# eli def funktio( a, b ) saa argumetit (100, 200) jos sanakirjassa ( a:100 , b:200)
# Jee! Tupleille on olemassa samankaltainen * -jutu.


parametrit = {
    "host" :'localhost',
    'database' :'ankkalinna',
    'user' : 'topi',
    'password' : ''
            }


yhteys = mariadb.connect(**parametrit)

sql = f"SELECT etunimi FROM ankkalinnalainen where sukunimi ='ankka'"
print(sql)
kursori = yhteys.cursor()
kursori.execute(sql)
tulos = kursori.fetchall()

print(tulos)


'''
import mariadb

# connection parameters
conn_params= {
    "user" : "example_user",
    "password" : "GHbe_Su3B8",
    "host" : "localhost",
    "database" : "test"
}

# Establish a connection
connection= mariadb.connect(**conn_params)

cursor= connection.cursor()

# Populate countries table  with some data
cursor.execute("INSERT INTO countries(name, country_code, capital) VALUES (?,?,?)",
               ("Germany", "GER", "Berlin"))

# retrieve data
cursor.execute("SELECT name, country_code, capital FROM countries")

# print content
row= cursor.fetchone()
print(*row, sep=' ')

# free resources
cursor.close()
connection.close()'''