'''T�m�n pit�isi lukea maiden suomenkieliset nimet ja koodit
tekstitiedostosta ja sy�tt�� nimet tietokantaan
aaaaaaa! '''

'''
import mysql.connector
#parametrit = {
    'host' :'localhost',
    'database' :'flight_game',
    'user' : 'root',
    'password' : 'paskatietokanta'

            }
'''

#yhteys = mysql.connector.connect(**parametrit)
'''kursori = yhteys.cursor()

sql0 = f"SELECT iso_country FROM kentat  "
print(sql0)
kursori.execute(sql0)
vastaus0 = kursori.fetchall()
print(vastaus0)
'''



f=open('C:\SQL\maailman maat 1.txt' ,mode="r", encoding="utf-16")
rivit=f.readlines()

print(rivit)


for a in rivit:
    #kursori = yhteys.cursor()
    #a.replace("\n", "")
    x = a.split("\t")[0]
    y = a.split("\t")[1]
    #z = y.replace("\n", "")
    z= y.strip()
    #print(x)
    #print(y)
    #print(z)

    sql = f"UPDATE kentat SET country_fi = '{z}' WHERE iso_country = '{x}'; "
    print(sql)


    #print(sql)
    #kursori.execute(sql)
    #yhteys.commit()







