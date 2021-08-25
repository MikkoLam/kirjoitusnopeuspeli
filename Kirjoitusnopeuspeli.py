# KIRJOITUSNOPEUSPELI
# Ohjelmoinut: Mikko Lampinen
# versio 1.0, maaliskuu 2021
# Ohjelma arpoo sanan, jonka käyttäjän tulee kirjoittaa mahdollisimman nopeasti
# Ohjelma tallentaa myös 10 parasta tulosta


def parhaat(sana):
    with open("best_"+str(sana)+".csv", "r") as bestfile:
        for row in bestfile:
            details = row.split(",")
            return details

def tallenna(tää_sana,rivi):
    with open("best_" + str(tää_sana) + ".csv", "w") as writefile:
        writefile.write(rivi)


tulokset = []
from time import time
import random
print("Kirjoitusnopeuspeli")
#import datetime
kaikki_sanat = ["kirjoitusnopeus", "omakotitalo", "rekvisiitta", "tiedonjano", "melkein",
                "onnettomuustutkintalautakunta", "niinkö", "apulaissheriffi"]

print("Kirjoita jokin seuraavista ja paina enter niin nopeasti kuin pystyt.")
print(kaikki_sanat)
nimi = input("Anna ensin nimesi: ")
# if nimi sisältää ","...

uudestaan = "k"

while uudestaan != "e":
    sekunnit = 36
    x = random.randint(0,7)
    sana = kaikki_sanat[x]
    print(" " + sana)
    t1 = time()
    vastaus = input (">")
    if vastaus == sana:
        t2 = time()
        sekunnit = int(1000*(t2-t1))/1000
        print("Hyvä, " + nimi + "!")
        print("Aikasi:", sekunnit, "s")
    else:
        print("Hups, väärin meni!")
    tulokset = parhaat(x)
    rivi = 100
    for i in range(0,22,2):
        tulos = float(tulokset[i])
        if sekunnit < tulos and sekunnit > 0:         # jos vastaajan sekunnit < tiedostossa olevan tulos
            tulokset.insert(i,str(sekunnit))   # työnnetään tuloksiin i kohtaan sekunnit
            tulokset.insert(i+1,nimi)   # ja seuraavaan kohtaan nimi
            rivi = int(i/2+1)
            sekunnit = 35          # sekunnit suureksi, ei inserttaa tietoja kahta kertaa, s=35 on samalla merkki tallennustarpeesta
    print("********************")
    print("  Parhaat tulokset")
    print("********************")
    for i in range(0,19,2):
        if int(i/2+1) == rivi:
            print(tulokset[i],"    ", tulokset[i + 1], "<-------------")
        else:
            print(tulokset[i],"    ", tulokset[i + 1])

    if sekunnit == 35:
        tallennettava = ""
        for item in tulokset:
            tallennettava += item + ","
        tallenna(x,tallennettava)
    uudestaan = input("Uusiksi? e=ei: ")
