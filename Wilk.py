from Zwierze import Zwierze
SILA = 9
INICJATYWA = 5
KOLOR = (0, 0, 0)


class Wilk(Zwierze):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='W'):
        super(Wilk, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other, Wilk)
        return czy_jest

    def _stworz_kopie(self, polozenie):
        owieczka = Wilk(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(owieczka)
        self._swiat.set_organizmy(organizmy)

    def napisz1(self):
        return "wilk"

    def napisz2(self):
        return "wilka"
