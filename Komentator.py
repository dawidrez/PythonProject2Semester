from Roslina import Roslina


class Komentator:

    def __init__(self):
        self.__komentarze = []

    # dodanie komentarza o nowym organizmie
    def nowy(self, organ):
        komentarz = "Na mapie pojawia sie " + organ.napisz1() + str(organ.get_polozenie())
        self.__komentarze.append(komentarz)

    def set_komentarze(self, komenatrze):
        self.__komentarze = komenatrze

    # poinformowanie o smierci organizmu oraz jego zabojcy
    def zabity(self, punkt_zabitego, punkt_zabijajacego, swiat):
        zabity = swiat.organizm_punkt(punkt_zabitego)
        zabojca = swiat.organizm_punkt(punkt_zabijajacego)
        zabity_czy_roslina = isinstance(zabojca, Roslina)
        zabojca_czy_roslina = isinstance(zabity, Roslina)
        komentarz = zabojca.napisz1()
        if zabity_czy_roslina is False and zabojca_czy_roslina is True:
            komentarz += " zjada "
        else:
            komentarz += " zabija "
        komentarz += zabity.napisz2()
        komentarz += str(punkt_zabitego)
        self.__komentarze.append(komentarz)

    # stworzenie komentarza o ucieczce
    def ucieczka(self, punkt_uciekajacego, punkt_atakujacego, swiat):
        uciekinier = swiat.organizm_punkt(punkt_uciekajacego)
        atakujacy = swiat.organizm_punkt(punkt_atakujacego)
        komentarz = uciekinier.napisz1()+" uciekl przed atakiem "+atakujacy.napisz2() + " na pole" + str(punkt_uciekajacego)
        self.__komentarze.append(komentarz)

    def odpieranie(self, punkt_zolwia, punkt_odpartego,  swiat):
        zolw = swiat.organizm_punkt(punkt_zolwia)
        atakujacy = swiat.organizm_punkt(punkt_odpartego)
        komentarz = zolw.napisz1()+" odparl atak "+atakujacy.napisz2()
        self.__komentarze.append(komentarz)

    def nowa_tura(self, tura):
        komentarz = "Nowa tura: " + str(tura)
        self.__komentarze.append(komentarz)

    def moce(self, czy_aktywna, cooldown):
        if czy_aktywna:
            komentarz = "Moc specjalna aktywna"
        elif cooldown <= 0:
            komentarz = "Mozna aktywowac moc specjalna"
        else:
            komentarz = "Nie mozna aktywowac mocy specjalnej"
        self.__komentarze.append(komentarz)

    def get_komentarze(self):
        return self.__komentarze
