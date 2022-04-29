class Organizm:
    def __init__(self, sila, inicjatywa, swiat, polozenie, wiek, kolor, obwod, znak):
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._swiat = swiat
        self._polozenie = polozenie
        self._wiek = wiek
        self._mozliwosc_ruchu = False
        self._zywy = True
        self._kolor = kolor
        self._obwod = obwod
        self._znak = znak
        komentator = self._swiat.get_komentator()
        komentator.nowy(self)

    # z listy pola usuwamy wszystkie pola, na ktorych jest jakis organizm
    def _tylko_wolne(self, pola):
        usuniete = 0
        rozmiar = len(pola)
        for i in range(0, rozmiar):
            tmp = self._swiat.organizm_punkt(pola[i - usuniete])
            if tmp is not None:
                pola.remove(pola[i - usuniete])
                usuniete += 1
        return pola

    def czy_zmiana_pola(self, polozenie):
        return False

    def czy_odpiera(self, polozenie):
        return False

    def czy_ucieczka(self, polozenie):
        return False

    def czy_efekt_zjedzenia(self, punkt):
        return False

    def czy_odporny_na_barszcz(self):
        return False

    def get_sila(self):
        return self._sila

    def get_mozliwosc_ruchu(self):
        return self._mozliwosc_ruchu

    def get_obwod(self):
        return self._obwod

    def get_znak(self):
        return self._znak

    def get_inicjatywa(self):
        return self._inicjatywa

    def get_wiek(self):
        return self._wiek

    def get_kolor(self):
        return self._kolor

    def get_polozenie(self):
        return self._polozenie

    def get_moc(self):
        return False

    def set_sila(self, sila):
        self._sila = sila

    def set_polozenie(self, polozenie):
        self._polozenie = polozenie

    def set_mozliwosc_ruchu(self, mozliwosc):
        self._mozliwosc_ruchu = mozliwosc

    def set_wiek(self, wiek):
        self._wiek = wiek

    def set_moc(self, moc):
        return 0

    def set_kierunek(self, kierunek):
        return 0

    def set_zycie(self, zycie):
        self._zywy = zycie

    def czy_zywy(self):
        return self._zywy

    def zapisz(self):
        zapis = self.get_znak() + ":" + str(self._polozenie.get_x()) + ":" + str(self._polozenie.get_y()) + ":" + str(self._sila) + ":" + str(self._wiek)
        return zapis
