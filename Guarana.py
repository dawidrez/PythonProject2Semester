from Roslina import Roslina
SILA = 0
INICJATYWA = 0
SZANSA = 2
KOLOR = (101, 0, 50)


class Guarana(Roslina):

    def __init__(self, punkt, swiat, sila=SILA, wiek=0, znak='G'):
        super(Guarana, self).__init__(sila, INICJATYWA, swiat, punkt, wiek, KOLOR, znak)

    def _szansa(self):
        return SZANSA

    def _stworz_kopie(self, polozenie):
        guarana = Guarana(polozenie, self._swiat)
        organizmy = self._swiat.get_organizmy()
        organizmy.append(guarana)
        self._swiat.set_organizmy(organizmy)

    def napisz1(self):
        return "Guarana"

    def napisz2(self):
        return "guarane"

    # po zjedzeniu guarany zwierze dostaje + 3 sily
    def czy_efekt_zjedzenia(self, punkt):
        tmp = self._swiat.organizm_punkt(punkt)
        tmp.set_sila(tmp.get_sila() + 3)
        self._swiat.dodaj_do_zabicia(self._polozenie, punkt)
        tmp.set_polozenie(self._polozenie)
        return True
