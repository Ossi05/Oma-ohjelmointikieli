# Oma-ohjelmointikieli
Mooc Python kursi osa 7:6 Oma ohjelmointikieli


Ohjelma muodostuu riveistä, joista jokainen on yksi seuraavista:

PRINT [arvo]: tulostaa annetun arvon
MOV [muuttuja] [arvo]: asettaa muuttujaan annetun arvon
ADD [muuttuja] [arvo]: lisää muuttujaan annetun arvon
SUB [muuttuja] [arvo}: vähentää muuttujasta annetun arvon
MUL [muuttuja] [arvo]: kertoo muuttujan annetulla arvolla
[kohta]:: määrittelee kohdan, johon voidaan hypätä muualta
JUMP [kohta]: hyppää annettuun kohtaan
IF [ehto] JUMP [kohta]: jos ehto pätee, hyppää annettuun kohtaan
END: lopettaa ohjelman
Ohjelmaa suoritetaan rivi kerrallaan ensimmäisestä rivistä aloittaen. Ohjelma päättyy, kun vastaan tulee komento END tai suoritus menee ohjelman viimeisen rivin yli.

Jokaisessa ohjelmassa on 26 muuttujaa, joiden nimet ovat A...Z. Jokaisen muuttujan arvo on 0 ohjelman alussa. Merkintä [muuttuja] viittaa tällaiseen muuttujaan.

Kaikki ohjelman käsittelemät arvot ovat kokonaislukuja. Merkintä [arvo] viittaa joko muuttujaan tai kokonaislukuna annettuun arvoon.

Merkintä [kohta] on mikä tahansa kohdan nimi, joka muodostuu pienistä kirjaimista a...z sekä numeroista 0...9. Kahdella kohdalla ei saa olla samaa nimeä.

Merkintä [ehto] tarkoittaa ehtoa muotoa [arvo] [vertailu] [arvo]. Tässä [vertailu] on aina yksi seuraavista: ==, !=, <, <=, > tai >=.


