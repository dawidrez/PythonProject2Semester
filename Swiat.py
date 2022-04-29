from Owca import Owca
import random
from Wilk import Wilk
from Mlecz import Mlecz
from Barszcz import Barszcz
from CyberOwca import CyberOwca
from Trawa import Trawa
from Lis import Lis
from Antylopa import Antylopa
from Zolw import Zolw
from Polozenie import Polozenie
from Czlowiek import Czlowiek
from WilczeJagody import WilczeJagody
from Guarana import Guarana
POCZATKOWA_ILOSC_ORGANIZMOW = 25
SZEROKOSC = 20
LICZBA_GATUNKOW = 11


class Swiat:

    def __init__(self, komentator):
        self.__x = 0
        self.__y = 0
        self.__komentator = komentator
        self.__do_zabicia = []
        self.__organizmy = []
        self.__tura = 0

    def __moc_czlowieka(self, organizm):
        moc = organizm.get_moc()
        cooldown = organizm.get_cooldown()
        self.__komentator.moce(moc, cooldown)

    def __zabij(self):
        for organizm in self.__organizmy:
            if organizm.czy_zywy() is False:
                self.__organizmy.remove(organizm)

    def __sortuj(self):
        self.__organizmy.sort(key=lambda x: (x.get_inicjatywa(), x.get_wiek()), reverse=True)

    def organizm_punkt(self, polozenie):
        for organizm in self.__organizmy:
            polozenie2 = organizm.get_polozenie()
            if polozenie.get_x() == polozenie2.get_x():
                if polozenie.get_y() == polozenie2.get_y():
                    return organizm
        return None

    def rozegraj_ture(self):
        self.__tura += 1
        self.__komentator.nowa_tura(self.__tura)
        for organizm in self.__organizmy:
            if isinstance(organizm, Czlowiek):
                self.__moc_czlowieka(organizm)
            organizm.set_wiek(organizm.get_wiek())
            organizm.set_mozliwosc_ruchu(True)
        self.__sortuj()
        for organizm in self.__organizmy:
            organizm.akcja()
        self.__zabij()

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_organizmy(self):
        return self.__organizmy

    def set_organizmy(self, organizmy):
        self.__organizmy = organizmy

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def dodaj_do_zabicia(self, polozenie_zabitego, polozenie_zabijajacego):
        zabity = self.organizm_punkt(polozenie_zabitego)
        self.__komentator.zabity(polozenie_zabitego, polozenie_zabijajacego, self)
        zabity.set_zycie(False)

    def set_kierunek(self, kierunek):
        for organizm in self.__organizmy:
            organizm.set_kierunek(kierunek)

    def ustaw_moc(self, moc):
        for organizm in self.__organizmy:
            organizm.set_moc(moc)

    def get_komentator(self):
        return self.__komentator

    def zapisz(self):
        plik = open("zapis.txt", mode="w")
        plik.write(str(self.__tura) + ":" + str(self.__x) + ":" + str(self.__y) + ":" + str(len(self.__organizmy)) + '\n')
        for organizm in self.__organizmy:
            plik.write(organizm.zapisz() + '\n')
        plik.close()

    def wczytaj(self):
        plik = open("zapis.txt", mode="r")
        self.__komentator.set_komentarze([])
        self.__organizmy.clear()
        data = plik.readline()
        data = data.split(':')
        self.__tura = int(data[0])
        self.__x = int(data[1])
        self.__y = int(data[2])
        ilosc_organizmow = int(data[3])
        for i in range(ilosc_organizmow):
            data = plik.readline()
            data = data.split(':')
            org = data[0]
            x = int(data[1])
            y = int(data[2])
            sila = int(data[3])
            wiek = int(data[4])
            if org == 'A':  # antylopa
                self.__organizmy.append(Antylopa(Polozenie(x, y), self, sila, wiek))
            elif org == 'c':  # cyberOwca
                self.__organizmy.append(CyberOwca(Polozenie(x, y), self, sila, wiek))
            elif org == 'L':  # lis
                self.__organizmy.append(Lis(Polozenie(x, y), self, sila, wiek))
            elif org == 'C':  # czlowiek
                kierunek = int(data[5])
                super_moc = bool(data[6])
                cooldown = int(data[7])
                self.__organizmy.append(Czlowiek(Polozenie(x, y), self, sila, wiek, kierunek, super_moc, cooldown))
            elif org == 'O':  # Owca
                self.__organizmy.append(Owca(Polozenie(x, y), self, sila, wiek))
            elif org == 'Z':  # Zolw
                self.__organizmy.append(Zolw(Polozenie(x, y), self, sila, wiek))
            elif org == 'W':  # Wilk
                self.__organizmy.append(Wilk(Polozenie(x, y), self, sila, wiek))
            elif org == 'G':  # Guarana
                self.__organizmy.append(Guarana(Polozenie(x, y), self, sila, wiek))
            elif org == 'B':  # Barszcz
                self.__organizmy.append(Barszcz(Polozenie(x, y), self, sila, wiek))
            elif org == 'J':  # Jagody
                self.__organizmy.append(WilczeJagody(Polozenie(x, y), self, sila, wiek))
            elif org == 'M':  # Mlecz
                self.__organizmy.append(Mlecz(Polozenie(x, y), self, sila, wiek))
            elif org == 'T':  # Trawa
                self.__organizmy.append(Trawa(Polozenie(x, y), self, sila, wiek))
        plik.close()
        return self.__x, self.__y

    # funckja tworzy organizmy na poczatku nowej rozgrywki
    def zaludnij(self):
        szerokosc = self.__x
        wysokosc = self.__y
        x = random.randint(0, szerokosc-1)
        y = random.randint(0, wysokosc-1)
        temp = Polozenie(x, y)
        czlowiek = Czlowiek(temp, self)
        self.__organizmy.append(czlowiek)
        for i in range(POCZATKOWA_ILOSC_ORGANIZMOW):
            while True:
                x = random.randint(0, szerokosc-1)
                y = random.randint(0, wysokosc-1)
                temp = Polozenie(x, y)
                organizm_punkt = self.organizm_punkt(temp)
                if organizm_punkt is None:
                    break
            random1 = random.randint(0, LICZBA_GATUNKOW-1)
            if random1 == 0:
                tmp = Owca(temp, self)
            elif random1 == 1:
                tmp = Trawa(temp, self)
            elif random1 == 2:
                tmp = Mlecz(temp, self)
            elif random1 == 3:
                tmp = Zolw(temp, self)
            elif random1 == 4:
                tmp = Lis(temp, self)
            elif random1 == 5:
                tmp = Guarana(temp, self)
            elif random1 == 6:
                tmp = WilczeJagody(temp, self)
            elif random1 == 7:
                tmp = Barszcz(temp, self)
            elif random1 == 8:
                tmp = Antylopa(temp, self)
            elif random1 == 9:
                tmp = Wilk(temp, self)
            elif random1 == 10:
                tmp = CyberOwca(temp, self)
            self.__organizmy.append(tmp)

    # funckja dodaje organizm do listy(dalsza czesc dodawania klikniecie)
    def dodaj_organizm(self, x, y, nr_gatunku):
        polozenie = Polozenie(x, y)
        if nr_gatunku == 0:
            tmp = Owca(polozenie, self)
        if nr_gatunku == 1:
            tmp = Wilk(polozenie, self)
        if nr_gatunku == 2:
            tmp = CyberOwca(polozenie, self)
        if nr_gatunku == 3:
            tmp = Lis(polozenie, self)
        if nr_gatunku == 4:
            tmp = Zolw(polozenie, self)
        if nr_gatunku == 5:
            tmp = Antylopa(polozenie, self)
        if nr_gatunku == 6:
            tmp = Trawa(polozenie, self)
        if nr_gatunku == 7:
            tmp = Mlecz(polozenie, self)
        if nr_gatunku == 8:
            tmp = Guarana(polozenie, self)
        if nr_gatunku == 9:
            tmp = WilczeJagody(polozenie, self)
        if nr_gatunku == 10:
            tmp = Barszcz(polozenie, self)
        self.__organizmy.append(tmp)
