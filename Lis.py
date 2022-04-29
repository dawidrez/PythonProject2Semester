from Zwierze import Zwierze
SILA = 3
INICJATYWA = 7
KOLOR = (240, 127, 0)


class Lis(Zwierze):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='L'):
        super(Lis, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other, Lis)
        return czy_jest

    def _stworz_kopie(self, polozenie):
        owieczka = Lis(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(owieczka)
        self._swiat.set_organizmy(organizmy)

    # podczas swojego przesuniecia lis nie wchodzi na pole z silniejszym przeciwnikiem
    def _specyficzne_przesuniecie(self):
        punkt = self.get_polozenie()
        pola = punkt.przesuniecie(self._swiat.get_x(), self._swiat.get_y())
        for pole in pola:
            tmp = self._swiat.organizm_punkt(pole)
            if tmp is not None:
                if self._czy_ten_gatunek(tmp):
                    pass
                elif tmp.get_sila() > self._sila:
                    pola.remove(pole)
        return pola

    def _czy_zwykly_ruch(self):
        return False

    def napisz1(self):
        return "Lis"

    def napisz2(self):
        return "lisa"
