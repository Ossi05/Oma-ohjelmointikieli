# tee ratkaisu tänne
import string


def suorita(ohjelma):
    
    # Muuttujat ja niiden arvot
    muisti = {}
    # Tuloste
    tuloste = []
    # Kohdat johon voi hypätä
    kohdat = {}

    # Lisää A-Z muuttujat ja niiden arvot muisti sanakirjaan
    for kirjain in string.ascii_uppercase:
        muisti[kirjain] = 0

    # [kohta]:: määrittelee kohdan, johon voidaan hypätä muualta
    for sijainti, sana in enumerate(ohjelma):
        if ":" in sana:
            nimi = sana.replace(":", "")
            kohdat[nimi] = sijainti
    
    luku = 0

    while luku < len(ohjelma):
        ohje = ohjelma[luku]
        osat = ohje.split(" ")

        # END: lopettaa ohjelman
        if osat[0] == "END":
            break
        
        # MOV [muuttuja] [arvo]: asettaa muuttujaan annetun arvon
        elif osat[0] == "MOV":
            if osat[2].isdigit():
                muisti[osat[1]] = int(osat[2])
            else:
                muisti[osat[1]] = muisti[osat[2]]
            
        # ADD [muuttuja] [arvo]: lisää muuttujaan annetun arvon
        elif osat[0] == "ADD":
            if not osat[2].isdigit():
                muisti[osat[1]] += muisti[osat[2]]
            else:
                muisti[osat[1]] += int(osat[2])
        
        # SUB [muuttuja] [arvo}: vähentää muuttujasta annetun arvon
        elif osat[0] == "SUB":
            if not osat[2].isdigit():
                muisti[osat[1]] -= muisti[osat[2]]
            else:
                muisti[osat[1]] -= int(osat[2])

        # MUL [muuttuja] [arvo]: kertoo muuttujan annetulla arvolla
        elif osat[0] == "MUL":
            if not osat[2].isdigit():
                muisti[osat[1]] *= muisti[osat[2]]
            else:
                muisti[osat[1]] *= int(osat[2])

        # PRINT [arvo]: tulostaa annetun arvon
        elif osat[0] == "PRINT":
            if not osat[1].isdigit():
                tuloste.append(muisti[osat[1]])
            else:
                tuloste.append(int(osat[1]))

        #JUMP [kohta]: hyppää annettuun kohtaan
        elif osat[0] == "JUMP":
            luku = kohdat[osat[1]]
      
        # IF [ehto] JUMP [kohta]: jos ehto pätee, hyppää annettuun kohtaan      
        elif osat[0] == "IF":
            if osat[3].isdigit() or osat[1].isdigit():
                if osat[3].isdigit() and osat[1].isdigit():
                    luku = vertailu(int(osat[1]), osat[2], int(osat[3]), kohdat, luku, osat[5])
                elif osat[3].isdigit():
                    luku = vertailu(muisti[osat[1]], osat[2], int(osat[3]), kohdat, luku, osat[5])
                else:
                    luku = vertailu(int(osat[1]), osat[2], muisti[osat[3]], kohdat, luku, osat[5])

            else:
                luku = vertailu(muisti[osat[1]], osat[2], muisti[osat[3]], kohdat, luku, osat[5])
            
    
            
        
        luku += 1
  
    return tuloste
    
# IF ehdon vertailu funktio
def vertailu(eka, merkki, toka, kohdat, luku, kohta):
    
    if merkki == "==" and eka == toka:
        luku = kohdat[kohta]
    
    elif merkki == "!=" and eka != toka:
        luku = kohdat[kohta]

    elif merkki == "<" and eka < toka:
        luku = kohdat[kohta]

    elif merkki == ">" and eka > toka:
        luku = kohdat[kohta]

    elif merkki == "<=" and eka <= toka:
        luku = kohdat[kohta]

    elif merkki == ">=" and eka >= toka:
        luku = kohdat[kohta]
    else:
        luku = luku
    
    return luku



if __name__ == "__main__":
    # Esimerkki 1:
    ohjelma1 = []
    ohjelma1.append("MOV A 1")
    ohjelma1.append("MOV B 2")
    ohjelma1.append("PRINT A")
    ohjelma1.append("PRINT B")
    ohjelma1.append("ADD A B")
    ohjelma1.append("PRINT A")
    ohjelma1.append("END")
    tulos = suorita(ohjelma1)
    print(tulos)

    # Esimerkki 2:
    ohjelma2 = []
    ohjelma2.append("MOV A 1")
    ohjelma2.append("MOV B 10")
    ohjelma2.append("alku:")
    ohjelma2.append("IF A >= B JUMP loppu")
    ohjelma2.append("PRINT A")
    ohjelma2.append("PRINT B")
    ohjelma2.append("ADD A 1")
    ohjelma2.append("SUB B 1")
    ohjelma2.append("JUMP alku")
    ohjelma2.append("loppu:")
    ohjelma2.append("END")
    tulos = suorita(ohjelma2)
    print(tulos)

    # Esimerkki 3 (kertoma):
    ohjelma3 = []
    ohjelma3.append("MOV A 1")
    ohjelma3.append("MOV B 1")
    ohjelma3.append("alku:")
    ohjelma3.append("PRINT A")
    ohjelma3.append("ADD B 1")
    ohjelma3.append("MUL A B")
    ohjelma3.append("IF B <= 10 JUMP alku")
    ohjelma3.append("END")
    tulos = suorita(ohjelma3)
    print(tulos)

    # Esimerkki 4 (alkuluvut):
    ohjelma4 = []
    ohjelma4.append("MOV N 50")
    ohjelma4.append("PRINT 2")
    ohjelma4.append("MOV A 3")
    ohjelma4.append("alku:")
    ohjelma4.append("MOV B 2")
    ohjelma4.append("MOV Z 0")
    ohjelma4.append("testi:")
    ohjelma4.append("MOV C B")
    ohjelma4.append("uusi:")
    ohjelma4.append("IF C == A JUMP virhe")
    ohjelma4.append("IF C > A JUMP ohi")
    ohjelma4.append("ADD C B")
    ohjelma4.append("JUMP uusi")
    ohjelma4.append("virhe:")
    ohjelma4.append("MOV Z 1")
    ohjelma4.append("JUMP ohi2")
    ohjelma4.append("ohi:")
    ohjelma4.append("ADD B 1")
    ohjelma4.append("IF B < A JUMP testi")
    ohjelma4.append("ohi2:")
    ohjelma4.append("IF Z == 1 JUMP ohi3")
    ohjelma4.append("PRINT A")
    ohjelma4.append("ohi3:")
    ohjelma4.append("ADD A 1")
    ohjelma4.append("IF A <= N JUMP alku")
    tulos = suorita(ohjelma4)
    print(tulos)

    # Testi 5
    ohjelma5 = []
    ohjelma5.append("PRINT A")
    ohjelma5.append("END")
    tulos = suorita(ohjelma5)
    print(tulos)
    