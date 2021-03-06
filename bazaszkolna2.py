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


class Uczen:
    def __init__(self, nazwa, klasa):
        self.nazwa = nazwa
        self.klasa = klasa


class Nauczyciel:
    def __init__(self, przedmiot, klasa):
        self.przedmiot = przedmiot
        self.klasa = klasa

    def nauczyciel_klasy(self):
        while True:
            nauczyciel_klasy = input()
            if not nauczyciel_klasy:
                break


def imie_nazwisko():
    imie_i_nazwisko = input()


# wczytanie danych z zewnetrznego pliku
while True:
    wejscie = input()
    if wejscie == "uczen":
        dane_uczen = Uczen(imie_nazwisko(), input())
        print(dane_uczen)
    if wejscie == "nauczyciel":
        imie_nazwisko()
        dane_nauczyciel = Nauczyciel(input())


    if wejscie == "wychowawca":
        imie_nazwisko()
        while True:
            ktore_klasy = input()
            if not ktore_klasy:
                continue
    if wejscie == "koniec":
        break
    else:
        continue    #TODO: czy to jest konieczne? może być przydatne, gdy mamy puste linie - sprawdzić


# # wczytanie danych z zewnetrznego pliku
# while True:
#     wejscie = input()
#     if wejscie == "uczen":
#         imie_nazwisko()
#         uczen_klasa = input()
#     if wejscie == "nauczyciel":
#         imie_nazwisko()
#         przedmiot = input()
#         while True:
#             nauczyciel_klasy = input()
#             if not nauczyciel_klasy:
#                 continue
#     if wejscie == "wychowawca":
#         imie_nazwisko()
#         while True:
#             ktore_klasy = input()
#             if not ktore_klasy:
#                 continue
#     if wejscie == "koniec":
#         break
#     else:
#         continue    #TODO: czy to jest konieczne? może być przydatne, gdy mamy puste linie - sprawdzić