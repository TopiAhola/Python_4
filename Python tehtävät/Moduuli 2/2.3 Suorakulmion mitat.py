
#Kysytään muuttujat
kanta=float(input("Anna suorakulmion kanta:"))
korkeus=float(input("Anna suorakulmion korkeus:"))

#Laskutoimitukset
piiri = (2 * kanta) + (2 * korkeus)
ala = kanta * korkeus

#Muutetaan tulokset stringeiksi tulostusta varten
piiristr = str(piiri)
alastr = str(ala)

#Tulostus:
print("Suorakulmion piiri on: "+piiristr)
print("Suorakulmion ala on: "+alastr)
