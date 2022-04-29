from Zwierze import Zwierze
from Polozenie import Polozenie
import random
SILA = 5
INICJATYWA = 4
COOLDOWN = 4
KOLOR = (255, 192, 203)


class Czlowiek(Zwierze):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, kierunek=0, super_moc=False, cooldown=0, znak='C'):
        super(Czlowiek, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)
        self.__kierunek = kierunek
        self.__cooldown = cooldown
        self.__super_moc = super_moc

    def _czy_zwykly_ruch(self):
        return False

    # logika poruszania sie czlowieka
    def _specyficzne_przesuniecie(self):
        x = self._polozenie.get_x()
        y = self._polozenie.get_y()
        polozenie = []
        if self.__kierunek == 0:
            # gora
            if y - 1 >= 0:
                polozenie.append(Polozenie(x, y - 1))
        elif self.__kierunek == 1:
            # lewo
            if x - 1 >= 0:
                polozenie.append(Polozenie(x - 1, y))
        elif self.__kierunek == 2:
            # prawo
            if x + 1 < self._swiat.get_x():
                polozenie.append(Polozenie(x + 1, y))
        else:
            # dol
            if y + 1 < self._swiat.get_y():
                polozenie.append(Polozenie(x, y + 1))
        return polozenie

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other,  Czlowiek)
        return czy_jest

    def napisz1(self):
        return "Czlowiek"

    def napisz2(self):
        return " czlowieka"

    def zapisz(self):
        zapis = super(Czlowiek, self).zapisz()
        zapis += ":" + str(self.__kierunek) + ":"
        if self.__super_moc:
            zapis += "1" + ":" + str(self.__cooldown)
        else:
            zapis += ":" + str(self.__cooldown)
        return zapis

    # co runde w czasie interakcji z uzytkownikiem uruchamiana jest ta funckja
    def set_moc(self, moc):
        if self.__super_moc is True and self.__cooldown > 0:
            # moc aktywna, zmiejszamy czas o 1
            self.__cooldown -= 1
        elif self.__super_moc is True and self.__cooldown == 0:
            # moc aktywna czas=0, wylaczamy moc oraz ustawiamy cooldown na 5 tur
            self.__super_moc = False
            self.__cooldown = COOLDOWN
        elif moc is True and self.__super_moc is False and self.__cooldown <= 0:
            # wlaczamy moc oraz ustawiamy czas trwania mocy na 5 tur
            self.__super_moc = True
            self.__cooldown = COOLDOWN
        else:
            self.__cooldown -= 1

    def set_kierunek(self, kierunek):
	    self.__kierunek = kierunek

    def get_cooldown(self):
        return self.__cooldown

    def get_moc(self):
        return self.__super_moc

    # jezeli czlowiek ma aktywna moc scpecjalna, to przy ataku na pole silniejszego organizmu moze jeszcze zmienic pole
    def czy_zmiana_pola(self, punkt):
        if self.__super_moc:
            komenatator = self._swiat.get_komentator()
            komenatator.ucieczka(self._polozenie, punkt, self._swiat)
            self.set_polozenie(punkt)
            pola = punkt.przesuniecie(self._swiat.get_x(), self._swiat.get_y())
            pola = self._tylko_wolne(pola)
            rozmiar = len(pola)
            indeks = random.randint(0, rozmiar - 1)
            self._polozenie = pola[indeks]
            return True
        return False

    def czy_ucieczka(self, polozenie):
        if self.__super_moc:
            komenatator = self._swiat.get_komentator()
            komenatator.ucieczka(self._polozenie, polozenie, self._swiat)
            pola = self._polozenie.przesuniecie(self._swiat.get_x(), self._swiat.get_y())
            for pole in pola:
                tmp = self._swiat.organizm_punkt(pole)
                if tmp is not None:
                    if tmp.get_sila() > self._sila:  # usuwamy pola, na ktorych znajduja sie silniejsi przeciwnicy
                        pola.remove(pole)
            rozmiar = len(pola)
            if rozmiar > 0:
                indeks = random.randint(0, rozmiar - 1)
                tmp = self._swiat.organizm_punkt(pola[indeks])
                if tmp is None:
                    self._polozenie = pola[indeks]
                else:
                    self.__kolizja(tmp)
                return True
            # czlowiek jest otoczony samymi silniejszymi zwierzeciami i nie ma dokad uciec
            # poniewaz jest niesmiertelny uznaje, ze atakujacy przegrywa ten pojedynek
            else:
                self._swiat.dodaj_do_zabicia(polozenie, self._polozenie)
                return True
        else:
            return False
