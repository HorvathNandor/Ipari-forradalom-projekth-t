minyear = 1700
maxyear = 2024
max_attempts = 3

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
                print(str(item2), end=" - ")  # Convert to string before printing
            print()
    else:
        print("A keresésnek nincs eredménye!")

adatok = []
try:
    with open("adatok2.txt", "r", encoding="utf-8") as f:
        for sor in f:
            try:
                kislista = sor.strip().split(";")
                kislista[0] = int(kislista[0])
                adatok.append(kislista)
            except ValueError:
                print("Hiba: Az évszám nem szám.")
except FileNotFoundError:
    print("Hiba: A fájl nem található.")

print("1. Adatok listázása")
print("2. Adatok listázása fájlba...")
print("3. Keresés évszám alapján...")

choice = int(input("Adj meg egy opciót: "))
if choice == 1:
    for item in adatok:
        for item2 in item:
            print(str(item2), end=" - ")
        print()
elif choice == 2:
    filename = input("Add meg a fájlnevet: ")
    filename = filename + ".txt"
    print("Az adatok mentve", filename, "fájlnéven")
    with open(filename, "a", encoding="utf-8") as file:
        for item in adatok:
            for item2 in item:
                print(str(item2), file=file)
            print("", file=file)
elif choice == 3:
    for attempt in range(max_attempts):
        print("--- Keresés ---")
        startyear = int(input(f"Adj meg egy kezdő évszámot {minyear} és {maxyear} között: "))

        if not (minyear <= startyear <= maxyear):
            print(f"Hibás évszám! Az évszámnak {minyear} és {maxyear} között kell lennie.")
            continue

        endyear = int(input(f"Adj meg egy befejező évszámot {minyear + 1} és {maxyear} között: "))

        if not (minyear + 1 <= endyear <= maxyear):
            print(f"Hibás évszám! Az évszámnak {minyear + 1} és {maxyear} között kell lennie.")
            continue

        if startyear > endyear:
            print("A kezdőévszám nem lehet nagyobb a befejező évszámnál!")
        else:
            search(startyear, endyear, adatok)
            break
    else:
        print(f"Túllépted a maximális próbálkozások számát ({max_attempts}). A keresés megszakítva.")