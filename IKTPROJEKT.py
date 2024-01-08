minyear = 1700
maxyear = 2024

while True:
    if minyear > maxyear:
        print("Kódhiba: A legkisebb évszám nem lehet nagyobb a legnagyobb évszámnál. A program nem tud elindulni!")
    else:
        break

def search(startyr, endyr, lst):
    result = []

    for item in lst:
        if item[0] >= startyr and item[0] <= endyr:
            result.append(item)

    if len(result) != 0:
        print("\n--- Találatok ---")
        for item in result:
            for item2 in item:
                print(item2, end=" - ")
            print()
    else:
        print("A keresésnek nincs eredménye!")

adatok = [
    [1712, "Vízkerék", "Thomas Newcomen", "Egyesült királyság"],
    [1760, "Textilgyártás mechanizálása", "Sir Richard Arkwright", "Egyesült királyság"],
    [1764, "Fonógép", "James Hargreaves", "Egyesült királyság"],
    [1765, "Gőzgép", "James Watt", "Egyesült királyság"],
    [1804, "Gőzvontatású vasút", "Richart Trevithick", "Egyesült királyság"],
    [1856, "Acélgyártás", "Henry Bessemer", "Egyesült királyság"],
    [1867, "Dinamó", "Werner von Siemens", "Németország"],
    [1870, "Telepített gépgyártás", "Henry Ford", "Amerikai Egyesült Államok"],
    [1876, "Telefon", "Alexander Graham Bell", "Amerikai Egyesült Államok"],
    [1879, "Elektromos izzó", "Thomas Edison", "Amerikai Egyesült Államok"],
    [1895, "Rádió", "Guglielmo Marconi", "Olaszország"],
    [1903, "Repülőgép", "Wright testvérek", "Amerikai Egyesült Államok"],
    [1908, "Ford T-Modell", "Henry Ford", "Amerikai Egyesült Államok"],
    [1913, "Tömegtermelés és szalaggyártás", "Henry Ford", "Amerikai Egyesült Államok"],
    [1917, "Fordson traktor", "Henry Ford", "Amerikai Egyesült Államok"],
    [1958, "Mikroelektronika", "Jack Kilby", "Amerikai Egyesült Államok"],
    [1969, "Internet", "Arpanet", "Amerikai Egyesült Államok"],
    [1970, "Asztali számítógép", "Intel corp.", "Amerikai Egyesült Államok"],
    [1973, "Mobiltelefon", "Martin Cooper", "Amerikai Egyesült Államok"],
    [1981, "Személyi számítógép", "IBM", "Amerikai Egyesült Államok"]
]

print("1. Adatok listázása")
print("2. Adatok listázása fájlba...")
print("3. Keresés évszám alapján...")

choice = int(input("Adj meg egy opciót: "))
if choice == 1:
    for item in adatok:
        for item2 in item:
            print(item2, end=" - ")
        print()
elif choice == 2:
    filename = input("Add meg a fájlnevet: ")
    filename = filename + ".txt"
    print("Az adatok mentve", filename, "fájlnéven")
    with open(filename, "a", encoding="utf-8") as file:
        for item in adatok:
            for item2 in item:
                print(item2, file=file)
            print("", file=file)
elif choice == 3:
    while True:
        print("--- Keresés ---")
        startyear = int(input(f"Adj meg egy kezdő évszámot {minyear} és {maxyear} között: "))
        if startyear < minyear:
            print(f"A kezdőévszám nem lehet kisebb {minyear} -nál/-nél!")
        elif startyear > maxyear:
            print(f"A kezdőévszám nem lehet nagyobb {maxyear} -nál/-nél!")
        else:
            endyear = int(input(f"Adj meg egy befejező évszámot {minyear + 1} és {maxyear} között: "))
            if endyear < minyear + 1:
                print(f"A befejezőévszám nem lehet kisebb {minyear + 1} -nál/-nél!")
            elif endyear > maxyear:
                print(f"A befejezőévszám nem lehet nagyobb {maxyear} -nál/-nél!")
            else:
                if startyear > endyear:
                    print("A kezdőévszám nem lehet nagyobb a befejező évszámnál!")
                else:
                    search(startyear, endyear, adatok)
                    break