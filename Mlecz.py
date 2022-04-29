from Roslina import Roslina
SILA = 0
INICJATYWA = 0
SZANSA = 1
KOLOR = (255, 255, 1)


class Mlecz(Roslina):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='M'):
        super(Mlecz, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _szansa(self):
        return SZANSA

    def _stworz_kopie(self, polozenie):
        mlecz = Mlecz(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(mlecz)
        self._swiat.set_organizmy(organizmy)

    def napisz1(self):
        return "Mlecz"

    def napisz2(self):
        return "mlecza"

    def akcja(self):
        for i in range(0, 2):
            super(Mlecz, self).akcja()
