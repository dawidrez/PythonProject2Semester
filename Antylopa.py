from Zwierze import Zwierze
from Polozenie import Polozenie
import random
SILA = 4
INICJATYWA = 4
KOLOR = (150, 75, 0)


class Antylopa(Zwierze):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='A'):
        super(Antylopa, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other, Antylopa)
        return czy_jest

    def _stworz_kopie(self, polozenie):
        antylopa = Antylopa(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(antylopa)
        self._swiat.set_organizmy(organizmy)

    def _specyficzne_przesuniecie(self):
        punkt = self.get_polozenie()
        pola = []
        x = self._swiat.get_x()
        y = self._swiat.get_y()
        if punkt.get_x() - 2 >= 0:
            pola.append(Polozenie(punkt.get_x()-2, punkt.get_y()))
        if punkt.get_y() - 2 >= 0:
            pola.append(Polozenie(punkt.get_x(), punkt.get_y() - 2))
        if punkt.get_x() + 2 < x:
            pola.append(Polozenie(punkt.get_x() + 2, punkt.get_y()))
        if punkt.get_y() + 2 < y - 1:
            pola.append(Polozenie(punkt.get_x(), punkt.get_y() + 2))
        return pola

    def czy_zwykly_ruch(self):
        return False

    def napisz1(self):
        return "Antylopa"

    def napisz2(self):
        return "antylope"

    # funckja odpowiedzialna  za unikniecie walki w przypadku kiedy antylopa sama zaatakowal
    def czy_zmiana_pola(self, polozenie):
        random1 = random.randint(0, 1)
        if random1 == 0:
            pola = polozenie.przesuniecie(self._swiat.get_x(), self._swiat.get_y())
            pola = self._tylko_wolne(pola)
            rozmiar = len(pola)
            if rozmiar > 0:
                random2 = random.randint(0, rozmiar - 1)
                self.set_polozenie(pola[random2])
                komentator = self._swiat.get_komentator()
                komentator.ucieczka(self._polozenie, polozenie, self._swiat)
                return True
            else:
                return False
        return False

    def czy_ucieczka(self, polozenie):
        random1 = random.randint(0, 1)
        if random1 == 0:
            pola = polozenie.przesuniecie(self._swiat.get_x(), self._swiat.get_y())
            pola = self._tylko_wolne(pola)
            rozmiar = len(pola)
            if rozmiar > 0:
                random2 = random.randint(0, rozmiar - 1)
                komentator = self._swiat.get_komentator()
                komentator.ucieczka(self._polozenie, polozenie, self._swiat)
                atakujacy = self._swiat.organizm_punkt(polozenie)
                atakujacy.set_polozenie(self._polozenie)
                self.set_polozenie(pola[random2])
                return True
        else:
            return False
        return False
