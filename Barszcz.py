from Roslina import Roslina
SILA = 10
INICJATYWA = 0
SZANSA = 1
KOLOR = (251, 12, 4)


class Barszcz(Roslina):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak="B"):
        super(Barszcz, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _szansa(self):
        return SZANSA

    def _stworz_kopie(self, polozenie):
        barszcz = Barszcz(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(barszcz)
        self._swiat.set_organizmy(organizmy)

    def napisz1(self):
        return "Barszcz"

    def napisz2(self):
        return "barszcz"

    def akcja(self):
        punkt = self._polozenie
        punkty = punkt.get_pola_dla_dzieci_roslina(self._swiat.get_x(), self._swiat.get_y())
        for pole in punkty:
            tmp = self._swiat.organizm_punkt(pole)
            if tmp is not None:
                if tmp.czy_odporny_na_barszcz() is False:
                    if tmp.get_moc() is False and tmp.czy_zywy() is True:
                        self._swiat.dodaj_do_zabicia(pole, punkt)
        super(Barszcz, self).akcja()

    # po zjedzeniu barszczu zwierze ginie
    def czy_efekt_zjedzenia(self, punkt):
        tmp = self._swiat.organizm_punkt(punkt)
        if tmp.get_moc() is False and tmp.czy_odporny_na_barszcz() is False:
            self._swiat.dodaj_do_zabicia(punkt, self._polozenie)
            self._swiat.dodaj_do_zabicia(self._polozenie, punkt)
        else:
            self._swiat.dodaj_do_zabicia(self._polozenie, punkt)
            tmp.set_polozenie(self._polozenie)
        return True

    def czy_odporny_na_barszcz(self):
        return True
