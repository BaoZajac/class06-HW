"""
Program do obsługi bazy szkolnej

Mamy trzy typy użytkowników:
    Wychowawca - ma przypisane klasy
    Nauczyciel - Mentor ma przypisany przedmiot i wiele klas
    Uczeń - jest przypisany do jednej klasy

Napisz program, który ze standardowego wyjścia pobierze dane w następujący sposób:
    Pobierze typ użytkownika: (uczeń, nauczyciel, wychowawca, koniec), oraz Imię i nazwisko Jeśli pobrano koniec, przejdź do kroku 5
    Jeśli typ użytkownika to uczeń, pobierz jedną linię - będzie to nazwa klasy (np. 3C), przejdź do kroku 1
    Jeśli typ użytkownika to nauczyciel, pobierz 1 linię - nazwę przedmiotu prowadzonego, a następnie w nowych liniach nazwy klas, aż do otrzymania pustej linii. Przejdź do korku 1
    Jeśli typ użytkownika to wychowawca, pobieraj w nowych liniach nazwy klas, które prowadzi wychowawca, aż do pustej linii, przejdź do kroku 1
    Wykonaj polecenie na podstawie przekazanego argumentu

Program będzie wykonywany w następujący sposób (zakładając nazwę pliku bazaszkolna2.py)
python bazaszkolna2.py <phrase>
jeśli phrase to nazwa klasy: program wypisze wychowawcę i uczniów w klasie
jeśli phrase to wychowawca: wypisz wszystkich uczniów, których prowadzi wychowawca
jeśli phrase to nauczyciel: wypisz wychowawców wszystkich klas, z którym ma zajęcia nauczyciel
jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
"""

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
print("NAUCZYCIELE: ", nauczyciele)
print("KLASY: ", klasy)
