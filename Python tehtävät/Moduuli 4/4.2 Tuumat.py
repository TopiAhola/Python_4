'''Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan
kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm'''


# try-except pakottaa oikeanlaisen syötteen
# if tuumat<0 break rikkoo silmukan ennen kun tulostus tapahtuu
# eli negatiivinen syöte lopettaa, ei tulosta negatiivista numeroa

tuumat=float(0)
while True:
    try:
        tuumat = float(input("Anna tuumat: "))

        if tuumat < 0:
            break


        print(f"{tuumat} tuumaa on {tuumat * 2.54}cm. ")

    except ValueError:
            print("Anna tuumat numerona. Anna negatiivinen numero lopettaaksesi.")


print("Lopetetaan.")

