import math
pi = math.pi
lista = ["gömb", "hasáb", "henger", "kocka", "téglatest"]


def szamadas(s):
     while True:
            try:
                print(s,end=" ")
                value = float(input())
                return value
            except ValueError:
                print ("Kérlek számot adj meg! Ha nincs adat akkor 0-t írj be! ")

def kocka():
    kocka_oldal = szamadas("Mekkora a kocka oldala? ")
    kocka_felszin = szamadas("Mekkora a kocka felszíne? ")
    kocka_terfogat = szamadas("Mekkora a kocka térfogata? ")
    if kocka_oldal == 0:
        if kocka_felszin != 0:
            kocka_oldal = math.sqrt(kocka_felszin / 6)
        elif kocka_terfogat != 0:
            kocka_oldal = kocka_terfogat ** (1/3)
    
    if kocka_terfogat == 0:
        kocka_terfogat = kocka_oldal ** 3
    
    if kocka_felszin == 0:
        kocka_felszin = kocka_oldal ** 2 * 6
    

    print(f"A kocka oldala: {kocka_oldal} \nA kocka felszíne: {kocka_felszin} \nA kocka térfogata: {kocka_terfogat}")

def teglatest():
    teglatest_hossz = szamadas("Mekkora a téglatest hossza? ")
    teglatest_szelesseg = szamadas("Mekkora a téglatest szélessége? ")
    teglatest_magassag = szamadas("Mekkora a téglatest magassága? ")
    teglatest_felszin = szamadas("Mekkora a téglatest felszíne? ")
    teglatest_terfogat = szamadas("Mekkora a téglatest térfogata? ")
    if teglatest_hossz == 0:
        if teglatest_felszin != 0:
            teglatest_hossz = (teglatest_felszin / 2 - teglatest_szelesseg * teglatest_magassag) / (teglatest_magassag + teglatest_szelesseg)
        elif teglatest_terfogat != 0:
            teglatest_hossz = teglatest_terfogat / teglatest_szelesseg / teglatest_magassag
    if teglatest_szelesseg == 0:
        if teglatest_felszin != 0:
            teglatest_szelesseg = (teglatest_felszin / 2 - teglatest_hossz * teglatest_magassag) / (teglatest_hossz + teglatest_magassag)
        elif teglatest_terfogat != 0:
            teglatest_szelesseg = teglatest_terfogat / teglatest_hossz / teglatest_magassag
    if teglatest_magassag == 0:
        if teglatest_felszin != 0:
            teglatest_magassag = (teglatest_felszin / 2 - teglatest_hossz * teglatest_szelesseg) / (teglatest_hossz + teglatest_szelesseg)
        elif teglatest_terfogat != 0:
            teglatest_magassag = teglatest_terfogat / teglatest_hossz / teglatest_szelesseg
    if teglatest_felszin == 0:
        teglatest_felszin = 2 * (teglatest_hossz * teglatest_szelesseg + teglatest_hossz * teglatest_magassag + teglatest_szelesseg * teglatest_magassag)
    if teglatest_terfogat == 0:
        teglatest_terfogat = teglatest_hossz * teglatest_szelesseg * teglatest_magassag
    
    print(f"A téglatest hossza: {teglatest_hossz} \nA téglatest szélessége: {teglatest_szelesseg} \nA téglatest magassága: {teglatest_magassag} \nA téglatest felszíne: {teglatest_felszin} \nA téglatest térfogata: {teglatest_terfogat}")

def hasab():
    alapterulet_oldala = szamadas("Mekkora az alapterület oldala? ")
    alapterulet_terulete = szamadas("Mekkora az alapterület területe? ")
    hasab_magassaga = szamadas("Mekkora a hasáb magassága? ")
    hasab_felszine = szamadas("Mekkora a hasáb felszíne? ")
    hasab_terfogata = szamadas("Mekkora a hasáb térfogata? ")
    if alapterulet_oldala == 0: 
        if alapterulet_terulete != 0:
            alapterulet_oldala = alapterulet_terulete ** (1/2)
        elif hasab_terfogata != 0:
            alapterulet_oldala = (hasab_terfogata / hasab_magassaga) ** (1/2)        
    if alapterulet_terulete == 0:
        alapterulet_terulete = alapterulet_oldala ** 2
    if hasab_magassaga == 0:
        if hasab_felszine != 0:
            hasab_magassaga = (hasab_felszine - 2 * alapterulet_oldala) / (4 * alapterulet_oldala)
        elif hasab_terfogata != 0:
            hasab_magassaga = hasab_terfogata / alapterulet_terulete
    if hasab_felszine == 0:
        hasab_felszine = 2 * alapterulet_terulete + 4 * alapterulet_oldala * hasab_magassaga
    if hasab_terfogata == 0:
        hasab_terfogata = (alapterulet_oldala ** 2) * hasab_magassaga
    
    print(f"Az alapterület oldala: {alapterulet_oldala} \nAz alapterület területe: {alapterulet_terulete} \nA hasáb magassága: {hasab_magassaga} \nA hasáb felszíne: {hasab_felszine} \nA hasáb térfogata: {hasab_terfogata}")

def henger():
    alapterulet_sugara = szamadas("Mekkora az alapterület sugara? ")
    alapterulet_kerulete = szamadas("Mekkora az alapterület kerülete? ")
    alapterulet_terulete = szamadas("Mekkora az alapterület területe? ")
    henger_magassaga = szamadas("Mekkora a henger magassága? ")
    henger_felszine = szamadas("Mekkora a henger felszíne? ")
    henger_terfogata = szamadas("Mekkora a henger térfogata? ")
    if alapterulet_sugara == 0:
        if alapterulet_kerulete !=0 :
            alapterulet_sugara = alapterulet_kerulete / (2 * pi)
        elif alapterulet_terulete != 0:
            alapterulet_sugara = (alapterulet_terulete / pi) ** (1/2)
    if alapterulet_kerulete == 0:
        alapterulet_kerulete = alapterulet_sugara * 2 * pi
    if alapterulet_terulete == 0:
        alapterulet_terulete = alapterulet_sugara ** 2 * pi
    if henger_magassaga == 0:
        if henger_terfogata != 0:
            henger_magassaga = henger_terfogata / (alapterulet_sugara ** 2) / pi
        elif henger_felszine != 0:
            henger_magassaga = (henger_felszine - 2 * alapterulet_terulete) / (2 * pi * alapterulet_sugara)
    if henger_felszine == 0:
        henger_felszine = 2 * (alapterulet_sugara ** 2) * pi + 2 * alapterulet_sugara * pi * henger_magassaga
    if henger_terfogata == 0:
        henger_terfogata = (alapterulet_sugara ** 2) * pi * henger_magassaga
    
    print(f"A henger alapterületének sugara: {alapterulet_sugara} \nA henger alapterületének kerülete: {alapterulet_kerulete} \nA henger alapterületének területe: {alapterulet_terulete}\nA henger magassága: {henger_magassaga} \nA henger felszíne: {henger_felszine} \nA henger térfogata: {henger_terfogata}")
    
    

def gomb():
    gomb_atmero = szamadas("Mekkora a gömb átmérője? ")
    gomb_sugara = szamadas("Mekkora a gömb sugara? ")
    gomb_felszin = szamadas("Mekkora a gömb felszíne? ")
    gomb_terfogat = szamadas("Mekkora a gömb térfogata? ")
    if gomb_sugara == 0:
        if gomb_atmero != 0:
            gomb_sugara = gomb_atmero / 2
        elif gomb_felszin != 0:
            gomb_sugara = (gomb_felszin / (4 * pi)) ** (1/2)
        elif gomb_terfogat != 0:
            gomb_sugara = (gomb_terfogat * 3 / (4 * pi)) ** (1/3)
    if gomb_atmero == 0:
        gomb_atmero = gomb_sugara * 2
    if gomb_felszin == 0:
        gomb_felszin = 4 * gomb_sugara ** 2 * pi
    if gomb_terfogat == 0:
        gomb_terfogat = (4 * gomb_sugara ** 3 * pi) * (1/3) 
    print(f"A gömb átmérője: {gomb_atmero} \nA gömb sugara: {gomb_sugara} \nA gömb felszíne: {gomb_felszin} \n A gömb térfogata: {gomb_terfogat}")
    

def alakzat_kerdes():         
    while True:
        try:
            valasz = input(f"{lista} \nA kilépéshez: kilép \nHa nincs valamiről adat 0-t írj be! \nMilyen alakzatot szeretnél kiszámoltatni?  ")
            if valasz == "kilép":
                break
            if valasz not in lista:
                print("Kérlek a listából válassz! ")
            if valasz == "kocka":
                kocka()
            if valasz == "téglatest":
                teglatest()
            if valasz == "gömb":
                gomb()
            if valasz == "henger":
                henger()
            if valasz == "hasáb":
                hasab()
        except:
            print("Hiba történt! Kérlek próbáld újra")
            continue


alakzat_kerdes()