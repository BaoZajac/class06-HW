
import sys

wychowawstwo = {}
nauczyciele = {}
klasy = {}
zbior_nauczycieli = set()


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

# print("WYCHOWAWSTWO: ", wychowawstwo)
# print("NAUCZYCIELE: ", nauczyciele)
# print("KLASY: ", klasy)


# reakcja na komendę z wejścia standardowego
# dla nazwy klasy
if sys.argv[1] in klasy:
    print("DANE DLA KLASY \"{}\":".format(sys.argv[1]))
    for klucz in wychowawstwo:
        for konkretna_klasa in wychowawstwo[klucz]:
            if sys.argv[1] in konkretna_klasa:
                print("Wychowawca:", klucz)
    for klucz in klasy:
        if klucz == sys.argv[1]:
            print("Lista uczniów:")
            for element in klasy[klucz]:
                print(element)
# dla nazwiska wychowawcy
if sys.argv[1] in wychowawstwo:
    print("DANE DLA WYCHOWAWCY:", sys.argv[1])
    print("Lista uczniów:")
    for wychowawca in wychowawstwo:
        if wychowawca == sys.argv[1]:
            for element in wychowawstwo[wychowawca]:
                for dana_klasa in klasy:
                    if dana_klasa == element:
                        for idx in klasy[dana_klasa]:
                            print(idx)
# dla nazwiska nauczyciela
if sys.argv[1] in nauczyciele:
    print("DANE DLA NAUCZYCIELA:", sys.argv[1])
    print("Wychowawcy:")
    for nauczyciel in nauczyciele:
        if nauczyciel == sys.argv[1]:
            for dane_nauczyciela in nauczyciele[nauczyciel]:
                if dane_nauczyciela == "klasy":
                    for dana_klasa in nauczyciele[nauczyciel][dane_nauczyciela]:
                        for dany_wychowawca in wychowawstwo:
                            for element in wychowawstwo[dany_wychowawca]:
                                if element == dana_klasa:
                                    zbior_nauczycieli.add(dany_wychowawca)
    for idx in zbior_nauczycieli:
        print(idx)
else:
    print(sys.argv[1])
    print("Nie ma takiej klasy")

