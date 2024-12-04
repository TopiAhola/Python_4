import requests
import json

#Uusi peli testi
name = input("Anna nimi: ")
difficulty = input("Anna vaikeusaste: ")

pyyntö1 = f"http://127.0.0.1:3000/newgame/{name}/{difficulty}"
print(pyyntö1)
vastaus_raw1 = requests.get(pyyntö1)
print(vastaus_raw1)
vastaus1 = vastaus_raw1.json()
print(vastaus1)

while True:
    #Pelaa peliä testi:
    flight_type = input("Anna lennon luokka: ")
    destination = input("Anna icao-koodi: ")
    pyyntö2 = f"http://127.0.0.1:3000/{flight_type}/{destination}"
    print(pyyntö2)
    vastaus_raw2 = requests.get(pyyntö2)
    print(vastaus_raw2)
    vastaus2 = vastaus_raw2.json()
    print(vastaus2)

'''
#Testitulosteita: 
print(vastaus2["airports"][0])
print(vastaus2["airports"][1])
if vastaus2["airports"][0]["visited"]:t
    print("Kentällä on käyty")

print(vastaus2['name'],vastaus2['flight_type'],vastaus2['destination'])
'''