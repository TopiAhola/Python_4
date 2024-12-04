
player = {"name": "topi", "money":0, "co2":100}
flight1 = {"destination":"espoo","cost":50}
flight2 = {"destination":"hesa","cost":50}
flights = [flight1, flight2]
game_status = "testistatus"

data = {"player": player, "flights":flights, "game_status":game_status }

print(data)
print(data["player"]["name"])
print(data["player"]["money"])
print(data["game_status"])

import json

json_data = json.dumps(data)

print(json_data)
