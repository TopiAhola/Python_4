import requests


luku = int(input("Anna luku: "))

pyyntö = f"http://127.0.0.1:3000/alkuluku/{luku}"
print(pyyntö)
vastaus = requests.get(pyyntö).json()

print(vastaus)
