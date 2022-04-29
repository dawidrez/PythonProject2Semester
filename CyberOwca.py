from Zwierze import Zwierze
from Barszcz import Barszcz
from Polozenie import Polozenie
import math
SILA = 11
INICJATYWA = 4
KOLOR = (165, 130, 93)


class CyberOwca(Zwierze):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak="c"):
        super(CyberOwca, self).__init__(sila, INICJATYWA, swiat, punkt, wiek,  KOLOR, znak)

    def __oblicz(self, punkt):
        punkt2 = self.get_polozenie()
        roznica_x = punkt.get_x()-punkt2.get_x()
        roznica_y = punkt.get_y() - punkt2.get_y()
        return math.sqrt(roznica_x * roznica_x + roznica_y * roznica_y)

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other, CyberOwca)
        return czy_jest

    # cyberowca przesuwa sie w osi x do najblizszego barszczu, nastepnie w osi y
    def _specyficzne_przesuniecie(self):
        punkt = self.get_polozenie()
        pola = []
        for organizm in self._swiat.get_organizmy():
            czy_jest = isinstance(organizm, Barszcz)
            if czy_jest:
                if organizm.czy_zywy():
                    lista = (organizm.get_polozenie(), self.__oblicz(organizm.get_polozenie()))
                    pola.append(lista)
        if len(pola) == 0:
            return self._polozenie.przesuniecie(self._swiat.get_x(), self._swiat.get_y())
        pola.sort(key=lambda x: x[1], )
        przesuniecie = []
        if punkt.get_x() != pola[0][0].get_x():
            if punkt.get_x() > pola[0][0].get_x():
                przesuniecie.append(Polozenie(punkt.get_x() - 1, punkt.get_y()))
            else:
                przesuniecie.append(Polozenie(punkt.get_x() + 1, punkt.get_y()))
        else:
            if punkt.get_y() > pola[0][0].get_y():
                przesuniecie.append(Polozenie(punkt.get_x(), punkt.get_y() - 1))
            else:
                przesuniecie.append(Polozenie(punkt.get_x(), punkt.get_y() + 1))
        return przesuniecie

    def _stworz_kopie(self, polozenie):
        barszcz = CyberOwca(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(barszcz)
        self._swiat.set_organizmy(organizmy)

    def _czy_zwykly_ruch(self):
        return False

    def czy_odporny_na_barszcz(self):
        return True

    def napisz1(self):
        return "CyberOwca"

    def napisz2(self):
        return "cyberOwce"
