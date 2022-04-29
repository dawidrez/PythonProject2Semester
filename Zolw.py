from Zwierze import Zwierze
import random
SILA = 2
INICJATYWA = 1
KOLOR = (54, 88, 0)


class Zolw(Zwierze):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='Z'):
        super(Zolw, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _czy_ten_gatunek(self, other):
        czy_jest = isinstance(other, Zolw)
        return czy_jest

    def _stworz_kopie(self, polozenie):
        zolwik = Zolw(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(zolwik)
        self._swiat.set_organizmy(organizmy)

    def czy_odpiera(self, atakujacy):
        if atakujacy.get_sila() >= 5:
            return False
        punkt1 = self._polozenie
        punkt2 = atakujacy.get_polozenie()
        komentator = self._swiat.get_komentator()
        komentator.odpieranie(punkt1, punkt2, self._swiat)
        return True

    def napisz1(self):
        return "Zolw"

    def napisz2(self):
        return "zolwia"

    def akcja(self):
        random1 = random.randint(0, 3)
        if random1 == 0:
            super(Zolw, self).akcja()
