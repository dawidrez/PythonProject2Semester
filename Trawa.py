from Roslina import Roslina
SILA = 0
INICJATYWA = 0
SZANSA = 3
KOLOR = (1, 56, 1)


class Trawa(Roslina):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='T'):
        super(Trawa, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _stworz_kopie(self, polozenie):
        owieczka = Trawa(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(owieczka)
        self._swiat.set_organizmy(organizmy)

    def _szansa(self):
        return SZANSA

    def napisz1(self):
        return "Trawa"

    def napisz2(self):
        return "trawe"
