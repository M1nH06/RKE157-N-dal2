"""
päev = input("Mis päev on homme (tööpäev või puhkepäev)? ")
if päev == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif päev == "puhkepäev":
    print("Filmi aeg :D")
else:
    print("Ma ei saa aru, mida sa räägid :(")
"""

'''
raha = int(input("Kui palju raha on sul praegu? "))

if raha < 2500:
    print("Sul veel pole kahjuks piisavalt raha, aga kogu julgesti edasi :)")
elif raha == 2500:
    print("Sul on täpne kogus selle ostmiseks, aga kogu igaks juhuks natuke veel ;)")
else:
    print("Sul on piisavalt raha, et see telefon osta :D")
'''

eesmärk = 8000
sammud = int(input("Mitu sammu oled juba teinud? "))
protsent = float((sammud/eesmärk)*100)

if protsent <= 50:
    print("Liigu aina edasi ;). Oled teinud " + str(protsent) + "%")
elif protsent <= 75:
    print("Natuke veel ja saavutad eesmärgi!  Oled teinud " + str(protsent) + "%")
elif protsent <= 100:
    print("Peaaeeguuuu!! Oled teinud " + str(protsent) + "%")
else:
    print("Tubliii!!! :D  Oled teinud " + str(protsent) + "%")