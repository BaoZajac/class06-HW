
import sys

wychowawstwo = {}
nauczyciele = {}
klasy = {}


# wczytanie danych z zewnetrznego pliku i przypisywanie do odpowiednich grup danych
while True:
    wejscie = input()
    if wejscie == "uczen":
        osoba = input()
        klasa_ucznia = input()
        if not klasy.get(klasa_ucznia):
            klasy[klasa_ucznia] = []
        klasy[klasa_ucznia].append(osoba)
    elif wejscie == "nauczyciel":
        osoba = input()
        przedmiot = input()
        nauczyciele[osoba] = {"przedmiot": przedmiot, "klasy":[]}
        while True:
            klasy_nauczyciela = input()
            if not klasy_nauczyciela:
                break
            nauczyciele[osoba]["klasy"].append(klasy_nauczyciela)
    elif wejscie == "wychowawca":
        osoba = input()
        wychowawstwo[osoba] = []
        while True:
            klasy_wychowawcy = input()
            if not klasy_wychowawcy:
                break
            wychowawstwo[osoba].append(klasy_wychowawcy)
    elif wejscie == "koniec":
        break
    else:
        print("Błąd")
        break

print("WYCHOWAWSTWO: ", wychowawstwo)
# print("NAUCZYCIELE: ", nauczyciele)
# print("KLASY: ", klasy)


# reakcja na komendę z wejścia standardowego
if sys.argv[1] in klasy:
    print("Dane dla klasy {}:".format(sys.argv[1]))
    for klucz in wychowawstwo:
        for konkretna_klasa in wychowawstwo[klucz]:
            if sys.argv[1] in konkretna_klasa:
                print("Wychowawca:", klucz)
else:
    print(sys.argv[1])
    print("Nie ma takiej klasy")

