from Roslina import Roslina
SILA = 99
INICJATYWA = 0
SZANSA = 1
KOLOR = (101, 0, 152)


class WilczeJagody(Roslina):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='J'):
        super(WilczeJagody, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other, WilczeJagody)
        return czy_jest

    def _stworz_kopie(self, polozenie):
        jagody = WilczeJagody(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(jagody)
        self._swiat.set_organizmy(organizmy)

    def _szansa(self):
        return SZANSA

    # po zjedzeniu jaood zwierze ginie
    def czy_efekt_zjedzenia(self, punkt):
        tmp = self._swiat.organizm_punkt(punkt)
        if tmp.get_moc() is False:
            self._swiat.dodaj_do_zabicia(punkt, self._polozenie)
            self._swiat.dodaj_do_zabicia(self._polozenie, punkt)
        else:
            self._swiat.dodaj_do_zabicia(self._polozenie, punkt)
            tmp.set_polozenie(self._polozenie)
        return True

    def napisz1(self):
        return "Wilcze jagody"

    def napisz2(self):
        return "wilcze jagody"
