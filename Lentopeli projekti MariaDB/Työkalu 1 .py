'''
Tämä lukee icao koodit tekstitiedostosta, poistaa rivinvaihdot ja tyhjät rivit, antaa koodit listamuodossa
'''

f=open('C:\SQL\maat2.txt' ,"r")
lines=f.readlines()
lista=[]
for x in lines:
    y = x.replace("\n", "")
    if y != "":

        lista.append(y)

print(lista)