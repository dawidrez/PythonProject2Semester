from Zwierze import Zwierze
SILA = 4
INICJATYWA = 4
KOLOR = (255, 255, 255)


class Owca(Zwierze):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='O'):
        super(Owca, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other, Owca)
        return czy_jest

    def _stworz_kopie(self, polozenie):
        owieczka = Owca(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(owieczka)
        self._swiat.set_organizmy(organizmy)

    def napisz1(self):
        return "owca"

    def napisz2(self):
        return "owce"
