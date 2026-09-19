#Programmi algus 
#Programm küsib kasutajalt, mitu klaasi vett on ta juba joonud
#Kasutaja sisestab arvu
#Programm salvestab kasutaja sisestatud arvu muutujasse "kogus"
#Programm arvutab valemi ([klaaside_arv]*250/2000)*100% järgi, kui oletame et üks klaas on 250 ml ja soovitatav kogus on 2 l ehk 2000 ml, ning salvestab saadud protsendi muutujasse "protsent"
#Kui saadud protsent on alla 50, siis programm väljastab lause "Joo rohkem vett, su keha vajab seda :)!"
#Kui protsent on alla 100 aga üle 50, siis programm väljastab "Tubli! Jätka samas vaimus ;)!"
#Kui protsent on 100 või rohkem, siis programm väljastab "Suurepärane, oled joonud piisavalt vett :D!" 
#Programmi lõpp
 
kogus = int(input("Kui mitu klaasi vett oled joonud täna? "))
protsent = (kogus*250/2000)*100

if protsent < 50:
    print("Joo rohkem vett, su keha vajab seda! :)")
elif protsent < 100:
    print("Tubli! Jätka samas vaimus! ;)")
else:
    print("Suurepäerane! Oled joonud piisavalt vett täna. :D")