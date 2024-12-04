import requests


icao = input("Anna ICAO-koodi: ")

pyyntö = f"http://127.0.0.1:3000/kentta/{icao}"
print(pyyntö)
vastaus = requests.get(pyyntö).json()

print(vastaus)
