from Organizm import Organizm
import random
OBWOD = (255, 156, 0)  # zwierzeta i rosliny maja inne ramki dookola kwadraciku, aby łatwiej roznicac


class Zwierze(Organizm):

    def __init__(self, sila, inicjatywa, swiat, punkt, wiek, kolor, znak):
        super(Zwierze, self).__init__(sila, inicjatywa, swiat, punkt, wiek, kolor, OBWOD, znak)

    def __kolizja(self, broniacy):
        if broniacy.czy_efekt_zjedzenia(self._polozenie):  # zwierze zjadlo rosline ze specjalna umiejetnoscia
            return 0
        elif self.get_sila() >= broniacy.get_sila():
            if broniacy.czy_odpiera(self):
                # atak zsotal odparty przez zolwia
                return 0
            elif broniacy.czy_ucieczka(self.get_polozenie()):
                # ucieczka antylopy i czlowieka udana
                return 0
            else:
                self._swiat.dodaj_do_zabicia(broniacy.get_polozenie(), self.get_polozenie())
                self.set_polozenie(broniacy.get_polozenie())
        else:
            if self.czy_zmiana_pola(broniacy.get_polozenie()):
                # uniknelismy potyczki z silniejszym organizmem
                return 0
            else:
                punkt = self.get_polozenie()
                self._swiat.dodaj_do_zabicia(punkt, broniacy.get_polozenie())

    def __rozmnoz(self, other):
        punkt = self.get_polozenie()
        pola = punkt.get_pola_dla_dzieci_zwierze(other, self._swiat.get_x(), self._swiat.get_y())
        pola = self._tylko_wolne(pola)
        ilosc_miejsc = len(pola)
        if ilosc_miejsc == 0:
            return 0
        index = random.randint(0, ilosc_miejsc-1)
        self._stworz_kopie(pola[index])

    def _czy_zwykly_ruch(self):
        return True

    def _specyficzne_przesuniecie(self):
        return 0

    def akcja(self):
        if self.get_mozliwosc_ruchu() and self.czy_zywy():
            punkt = self._polozenie
            if self._czy_zwykly_ruch():
                pola = punkt.przesuniecie(self._swiat.get_x(), self._swiat.get_y())
            else:
                pola = self._specyficzne_przesuniecie()
            rozmiar = len(pola)
            if rozmiar == 0:  # brak wolnych miejsc do przesuniecia, zwierrze zostaje w miejscu
                return 0
            random1 = random.randint(0, rozmiar-1)
            tmp_pol = pola[random1]
            tmp = self._swiat.organizm_punkt(tmp_pol)
            if tmp is not None:
                tmp.set_mozliwosc_ruchu(False)
                if self._czy_ten_gatunek(tmp):
                    self.__rozmnoz(tmp)
                else:
                    self.__kolizja(tmp)
            else:
                self.set_polozenie(tmp_pol)
