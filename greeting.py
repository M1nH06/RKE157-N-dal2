#Programmi algus
#Programm küsib kasutajalt tema perekonnanime
#Kasutaja sisestab oma perekonnanime
#Programm salvestab kasutaja perekonnanime muutujasse “perekonnanimi”
#Programm küsib kasutajalt tema sugu, sisestades kas "m" või "n"
#Kasutaja sisestab tähe vastavalt tema soole
#Programm salvestab kasutaja sisestatud tähe muutujasse “sugu”
#Kui kasutaja on mees, siis annab programm väljundiks "Tere, härra [Perekonnanimi]!"
#Kui kasutaja on naine, siis annab programm väljundiks "Tere, proua [Perekonnanimi]!"
#Kui kasutaja sisestab midagi muud, siis programm annab väljundiks "Tere tulemast, [Perekonnanimi]"
#Programmi lõpp

perekonnanimi = input("Tere. Mis on Teie perekonnanimi? ")
sugu = input("Mis on Teie sugu? Sisestage 'm', kui olete meessoost või 'n', kui olete naissoost. ")

if sugu == "m":
    print(f"Tere, härra {perekonnanimi}!")
elif sugu == "n":
    print(f"Tere, proua {perekonnanimi}!")
else:
    print(f"Tere tulemast, {perekonnanimi}!")