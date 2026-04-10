import pickle
from typing import List

class Kontakt:
    def __init__(self, imie: str, nazwisko: str, telefon: str, email: str):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

class KsiazkaTeleadresowa:
    def __init__(self):
        self.ksiazka = []

    def dodaj_osobe(self, osoba: Kontakt):
        self.ksiazka.append(osoba)
        
