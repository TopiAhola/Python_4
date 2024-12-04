'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.

Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin
sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen
on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
'''

#Paikkakunta API
# http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API key}


# Sää API
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API_key}
# ei käytetä : &exclude={part}
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}


import requests

#Muuttujat pyyntöihin:
API_key = input("Anna Openweather API key: ")

#Palautettavien säätietojen raja. Kokeillan 1.
limit = 1

#Maakoodi voi olla tyhjä.
city_name = input("Anna kunnan nimi: ")
country_code = ""
state_code = ""

kunta_pyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_key}"
kunta_vastaus = requests.get(kunta_pyynto).json()
#print(kunta_vastaus)

#Tulostetaan kunnan nimi ja maa
print(f"{kunta_vastaus[0]['name']}, {kunta_vastaus[0]['country']}")

lat = kunta_vastaus[0]["lat"]
lon = kunta_vastaus[0]["lon"]
#part =



saa_pyynto = f" https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
saa_vastaus = requests.get(saa_pyynto).json()

#print(saa_vastaus)

# säätila saa_vastaus["weather"][0]["description"]
# weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}]
#lämpötila

#Muotoillaan vastaus:
saa = saa_vastaus["weather"][0]["description"]
temp_k = (saa_vastaus["main"]["temp"])
temp_c = temp_k - 273.15
print(f"Säätila: {saa}")
print(f"Lämpötila: {temp_c:4.1f} C")

