'''Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan
halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.'''

def pizza_hinta(halkaisija_cm, hinta_e):
    import math
    # ala neliömetreinä
    ala_m2 = math.pi * (halkaisija_cm / 100 / 2) ** 2
    #euroa per neliö
    e_m2 = hinta_e / ala_m2

    return e_m2

print("Verrataan kahta pizzaa.")
hinta1 = float(input("Pizzan 1. hinta (euroa): "))
halkaisija1 = float(input("Pizzan 1 halkaisija (cm): "))
hinta2 = float(input("Pizzan 2. hinta (euroa): "))
halkaisija2 = float(input("Pizzan 2 halkaisija (cm): "))

arvo1 = pizza_hinta(halkaisija1, hinta1)
arvo2 = pizza_hinta(halkaisija2, hinta2)

print(f" Pizzan 1 hinta on {arvo1:.2f}€/m^2")
print(f" Pizzan 2 hinta on {arvo2:.2f}€/m^2")

if arvo1 < arvo2:
    print("Pizza 1 on parempi vastine rahalle.")
elif arvo2 < arvo1:
    print("Pizza 2 on parempi vastine rahalle.")
else:
    print("Pizzat ovat yhtä hyvä vastine rahalle.")

