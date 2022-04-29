from Organizm import Organizm
import random
OBWOD = (0, 255, 0)  # obwodka rosliny zielona
PRAWDOPODOBIENSTWO = 20


class Roslina(Organizm):

    def __init__(self, sila, inicjatywa, swiat, punkt, wiek, kolor, znak):
        super(Roslina, self).__init__(sila, inicjatywa, swiat, punkt, wiek, kolor, OBWOD, znak)

    def __czy_rozsiewa(self):
        random1 = random.randint(0, PRAWDOPODOBIENSTWO-1)
        if self._szansa() > random1:
            return True
        return False

    # fucnkja sprawdzac czy dookola roslinki jest puste miejsce dla nowej roslinki
    # jezeli tak to zasiewa
    def __rozsiej(self):
        pola = self._polozenie.get_pola_dla_dzieci_roslina(self._swiat.get_x(), self._swiat.get_y())
        pola = self._tylko_wolne(pola)
        rozmiar = len(pola)
        if rozmiar > 0:
            random1 = random.randint(0, rozmiar-1)
            self._stworz_kopie(pola[random1])

    def akcja(self):
        if self._mozliwosc_ruchu:
            if self.__czy_rozsiewa():
                self.__rozsiej()
