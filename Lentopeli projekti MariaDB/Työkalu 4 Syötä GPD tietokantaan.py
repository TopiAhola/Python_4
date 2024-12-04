
import mysql.connector
parametrit = {
    "host" :'localhost',
    'database' :'flight_game',
    'user' : 'root',
    'password' : 'paskatietokanta'
            }


yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

teksti=open('C:\SQL\euroopan gdp 2.txt' ,"r")
rivit=teksti.readlines()

print(rivit)


for a in rivit:
    x = a.split("\t")[0]
    y = a.split("\t")[1]
    #z = y.replace("\n", "")
    z = y.strip()
    #print(x, z)


    sql = f"UPDATE kentat SET GDP = '{x}' WHERE iso_country = '{z}'; "

    # Poistetaan commit käytöstä tilapäisesti:
    print(sql)
    #kursori.execute(sql)
    #yhteys.commit()