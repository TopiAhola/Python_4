'''Kirjoita peli, jossa tietokone arpoo kokonaisluvun
väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti,
kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa
tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.'''


import random
luku = int(random.randint(1,10))


while True:
    try:
        arvaus = int(input("Arvaa numero väliltä 1-10. \n"))


        if arvaus > 10 or arvaus < 1:
            print("Pitää olla väliltä 1-10! \n")

        elif arvaus == luku:
            print("Oikein!")
            break
        elif arvaus < luku:
            print("Liian pieni. \n")
        elif arvaus > luku:
            print("Liian iso. \n")



    except ValueError:
            print("Pitää olla kokonaisluku!")