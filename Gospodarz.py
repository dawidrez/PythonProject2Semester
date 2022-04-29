from Komentator import Komentator
from Swiat import Swiat
from Input import Input
import sys
import pygame
from Polozenie import Polozenie
from Button import Button
SZEROKOSC = 20
POCZATEK_KOMENTARZY_X = 800
POCZATEK_KOMENATRZY_Y = 100
MAX_ILOSC_KOMENATRZY = 25
ODSTEP = 30
POCZATEK_STEROWANIA_X = 1400
DLUGOSC_BUTTONA = 100
POCZATEK_STEROWANIA_Y = 100
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)


class Gospodarz:

    def __init__(self):
        pygame.init()
        self.__czy_mozna_moc = True
        self.__czcionka_mala = pygame.font.Font("freesansbold.ttf", 15)
        self.__czcionka_duza = pygame.font.Font("freesansbold.ttf", 25)
        self.__ekran = pygame.display.set_mode((1900, 1000))
        self.__czy_nastepna = False
        self.__strona = 0
        pygame.display.set_caption("Dawid Rezmer 184250")
        self.__szerokosc = 1900
        self.__wysokosc = 1000
        self.__komentator = Komentator()
        self.__swiat = Swiat(self.__komentator)
        wybor = self.__interakcja1()
        if wybor == 1:
            self.__interakcja2()
            self.__swiat.zaludnij()
        elif wybor == 2:
            self.__swiat.wczytaj()
        else:
            return
        self.__x = self.__swiat.get_x()
        self.__y = self.__swiat.get_y()
        self.__narysuj_plansze(self.__swiat.get_organizmy())
        if self.__interakcja():
            self.__rozegraj_ture()

    def __rozegraj_ture(self):
        self.__strona = 0
        self.__czy_nastepna = False
        self.__komentator.set_komentarze([])
        self.__swiat.rozegraj_ture()
        self.__narysuj_plansze(self.__swiat.get_organizmy())
        if self.__interakcja():
            self.__rozegraj_ture()

    def __interakcja(self):
        self.__czy_mozna_moc = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__czy_dodac_organizm()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    if self.__czy_mozna_moc:
                        self.__swiat.ustaw_moc(False)
                        self.__czy_mozna_moc = False
                    return True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    kierunek = 0
                    self.__swiat.set_kierunek(kierunek)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    kierunek = 1
                    self.__swiat.set_kierunek(kierunek)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    kierunek = 2
                    self.__swiat.set_kierunek(kierunek)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    kierunek = 3
                    self.__swiat.set_kierunek(kierunek)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    if self.__czy_nastepna is True:
                        self.__strona += 1
                        self.__narysuj_plansze(self.__swiat.get_organizmy())
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    if self.__strona > 0:
                        self.__strona -= 1
                        self.__narysuj_plansze(self.__swiat.get_organizmy())
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    if self.__czy_mozna_moc:
                        self.__swiat.ustaw_moc(True)
                        self.__czy_mozna_moc = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    self.__x, self.__y = self.__swiat.wczytaj()
                    self.__narysuj_plansze(self.__swiat.get_organizmy())
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.__swiat.zapisz()

    def __interakcja1(self):
        self.__ekran.fill(BIALY)
        text_surf = self.__czcionka_duza.render("Jezeli chcesz zaczac nowa gre, kliknij 1."
                                                " Jezeli chcesz wczytac wcisnij 2.", True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(self.__szerokosc/2, 30))
        self.__ekran.blit(text_surf, text_rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    return 1
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    return 2

    def __interakcja2(self):
        pierwsze = Input(self.__szerokosc / 2, 60, 100,
                         self.__czcionka_duza, self.__ekran)  # wymiary na idealne polozenie
        drugie = Input(self.__szerokosc / 2, 60, 100,
                       self.__czcionka_duza, self.__ekran)  # wymiary na idealne polozenie
        for i in range(2):
            while True:
                event = pygame.event.get()
                if i == 0:
                    wynik = pierwsze.update(event)
                else:
                    wynik = drugie.update(event)
                if wynik is not None:
                    if int(wynik) > 7 and int(wynik) < 31:  # wyjatek przy nie pisanie niczego obsluzyc
                        if i == 0:
                            self.__swiat.set_x(int(wynik))
                        else:
                            self.__swiat.set_y(int(wynik))
                        break
                self.__ekran.fill(BIALY)
                if i == 0:
                    text_surf = self.__czcionka_duza.render("Wpisz szerokosc planszy(8-30)", True, (0, 0, 0))
                else:
                    text_surf = self.__czcionka_duza.render("Wpisz wysokosc planszy(8-30)", True, (0, 0, 0))
                text_rect = text_surf.get_rect(center=(self.__szerokosc / 2, 30))
                self.__ekran.blit(text_surf, text_rect)
                if i == 0:
                    pierwsze.draw()
                else:
                    drugie.draw()
                pygame.display.flip()

    def __narysuj_plansze(self, organizmy, kontrolka = 0):
        if kontrolka == 0:
            self.__ekran.fill((0, 0, 0))
        szerokosc = (int(self.__x)) * SZEROKOSC + 3  # zeby organizmy nie nachodzily na bandy
        wysokosc = (int(self.__y)) * SZEROKOSC + 3
        pygame.draw.rect(self.__ekran, BIALY, pygame.Rect(0, 0, szerokosc, wysokosc), 1)
        for organizm in organizmy:
            x = int(organizm.get_polozenie().get_x()) * SZEROKOSC + 1
            y = int(organizm.get_polozenie().get_y()) * SZEROKOSC + 1
            kolor = organizm.get_kolor()
            kolor_ramki = organizm.get_obwod()
            pygame.draw.rect(self.__ekran, kolor, pygame.Rect(x, y, SZEROKOSC, SZEROKOSC))
            pygame.draw.rect(self.__ekran, kolor_ramki, pygame.Rect(x, y, SZEROKOSC, SZEROKOSC), 2)
        self.__narysuj_komentarze()
        self.__dodaj_legende()
        self.__dodaj_sterowanie()
        pygame.display.flip()

    def __narysuj_komentarze(self):
        komentarze = self.__komentator.get_komentarze()
        ilosc = len(komentarze)
        if self.__strona == 0:
            beg = 0
        else:
            beg = self.__strona * MAX_ILOSC_KOMENATRZY - 1
            text_surf = self.__czcionka_mala.render("Aby zobaczyć poprzednią strone kliknij m", True, BIALY)
            self.__ekran.blit(text_surf, (POCZATEK_KOMENTARZY_X, 60)) #60 to wysokosc napisu na ekranie
        if ilosc > (self.__strona + 1) * MAX_ILOSC_KOMENATRZY:
            max = MAX_ILOSC_KOMENATRZY
            text_surf = self.__czcionka_mala.render("Aby zobaczyć nastepna strone kliknij b", True, BIALY)
            self.__czy_nastepna = True
            self.__ekran.blit(text_surf, (POCZATEK_KOMENTARZY_X, 40)) #40 to wysokosc napisu na ekranie
        else:
            self.__czy_nastepna = False
            max = ilosc
        for i in range(beg, max):
            text_surf = self.__czcionka_duza.render(komentarze[i], True, BIALY)
            wysokosc = POCZATEK_KOMENATRZY_Y + 25 * (i - self.__strona * MAX_ILOSC_KOMENATRZY)  # wysokosc czcinkki plus 5 pixeli przerwy
            self.__ekran.blit(text_surf, (POCZATEK_KOMENTARZY_X, wysokosc))

    def __dodaj_sterowanie(self):
        text_surf = self.__czcionka_duza.render("q- koniec programu", True, BIALY)
        self.__ekran.blit(text_surf, (POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y))
        text_surf = self.__czcionka_duza.render("p- wlaczenie mocy specjalnej", True, BIALY)
        self.__ekran.blit(text_surf, (POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + ODSTEP))
        text_surf = self.__czcionka_duza.render("n- nastepna tura", True, BIALY)
        self.__ekran.blit(text_surf, (POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 2*ODSTEP))
        text_surf = self.__czcionka_duza.render("s- zapis do pliku", True, BIALY)
        self.__ekran.blit(text_surf, (POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y+3*ODSTEP))
        text_surf = self.__czcionka_duza.render("l- wczytanie z pliku", True, BIALY)
        self.__ekran.blit(text_surf, (POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y+4*ODSTEP))

    def __dodaj_legende(self):
        # wyswietlamy  menu z kolorami organizmow, kolory sa liczby w nawiasach to konkretne kolory w systemie rgb
        wysokosc = (int(self.__y)) * SZEROKOSC + 40  # 1 wpis w legendzie bedzie zawsze 40 pixeli pod mapa
        pygame.draw.rect(self.__ekran, CZARNY, pygame.Rect(SZEROKOSC, wysokosc, SZEROKOSC, SZEROKOSC))  # liczby to umiejscowienei na mapie
        pygame.draw.rect(self.__ekran, (255, 156, 0), pygame.Rect(SZEROKOSC, wysokosc, SZEROKOSC, SZEROKOSC), 2)  # wilk w tuplach kolory zwierzecia i obwodki
        text_surf = self.__czcionka_mala.render("-Wilk", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc))  # tekst na takie samej wysokosci, 15pxl za koncem figury

        pygame.draw.rect(self.__ekran, BIALY, pygame.Rect(SZEROKOSC, wysokosc + ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (255, 156, 0), pygame.Rect(SZEROKOSC, wysokosc + ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Owca", True, BIALY)  # 2 to szerokosc ramki
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + ODSTEP))

        pygame.draw.rect(self.__ekran, (150, 75, 0), pygame.Rect(SZEROKOSC, wysokosc + 2*ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (255, 156, 0), pygame.Rect(SZEROKOSC, wysokosc + 2*ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("Antylopa", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 2 * ODSTEP))

        pygame.draw.rect(self.__ekran, (255, 192, 203), pygame.Rect(SZEROKOSC, wysokosc + 3*ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (255, 156, 0), pygame.Rect(SZEROKOSC, wysokosc + 3*ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Czlowiek", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 3 * ODSTEP))

        pygame.draw.rect(self.__ekran, (54, 88, 0), pygame.Rect(SZEROKOSC, wysokosc + 4*ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (255, 156, 0), pygame.Rect(SZEROKOSC, wysokosc + 4*ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Zolw", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 4 * ODSTEP))

        pygame.draw.rect(self.__ekran, (240, 127, 0), pygame.Rect(SZEROKOSC, wysokosc + 5*ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (255, 156, 0), pygame.Rect(SZEROKOSC, wysokosc + 5*ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Lis", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 5 * ODSTEP))

        pygame.draw.rect(self.__ekran, (165, 130, 93), pygame.Rect(SZEROKOSC, wysokosc + 6 * ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (255, 156, 0), pygame.Rect(SZEROKOSC, wysokosc + 6 * ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-CyberOwca", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 6 * ODSTEP))

        pygame.draw.rect(self.__ekran, (101, 0, 50), pygame.Rect(SZEROKOSC, wysokosc + 7*ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (0, 255, 0), pygame.Rect(SZEROKOSC, wysokosc + 7*ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Guarana", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 7 * ODSTEP))

        pygame.draw.rect(self.__ekran, (101, 0, 152), pygame.Rect(SZEROKOSC, wysokosc + 8 * ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (0, 255, 0), pygame.Rect(SZEROKOSC, wysokosc + 8 * ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Jagody", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 8 * ODSTEP))

        pygame.draw.rect(self.__ekran, (251, 12, 4), pygame.Rect(SZEROKOSC, wysokosc + 9 * ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (0, 255, 0), pygame.Rect(SZEROKOSC, wysokosc + 9 * ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Barszcz", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 9 * ODSTEP))

        pygame.draw.rect(self.__ekran, (1, 56, 1), pygame.Rect(SZEROKOSC, wysokosc + 10 * ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (0, 255, 0), pygame.Rect(SZEROKOSC, wysokosc + 10 * ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Trawa", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 10 * ODSTEP))

        pygame.draw.rect(self.__ekran, (255, 255, 1), pygame.Rect(SZEROKOSC, wysokosc + 11 * ODSTEP, SZEROKOSC, SZEROKOSC))
        pygame.draw.rect(self.__ekran, (0, 255, 0), pygame.Rect(SZEROKOSC, wysokosc + 11 * ODSTEP, SZEROKOSC, SZEROKOSC), 2)
        text_surf = self.__czcionka_mala.render("-Mlecz", True, BIALY)
        self.__ekran.blit(text_surf, (2*SZEROKOSC+15, wysokosc + 11 * ODSTEP))

    def __wyswietl_opcje_interakcja(self):
        # funckja generuje przyciski do dodawania zwierzat
        buttony = []  # polozenie tych przyskow bedzie pod menu ze sterowaniem(6* odstep jest to polozenie od razu pod menu)
        # kazdy przycisk jest na tej samej szerokosci, nizej o ODSTEP
        button = Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 6 * ODSTEP, self.__ekran, "Owca")
        buttony.append(button)
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 7 * ODSTEP, self.__ekran, "Wilk"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 8 * ODSTEP, self.__ekran, "CyberOwca"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 9 * ODSTEP, self.__ekran, "Lis"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 10 * ODSTEP, self.__ekran, "Zolw"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 11 * ODSTEP, self.__ekran, "Antylopa"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 12 * ODSTEP, self.__ekran, "Trawa"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 13 * ODSTEP, self.__ekran, "Mlecz"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 14 * ODSTEP, self.__ekran, "Guarana"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 15 * ODSTEP, self.__ekran, "Wilcze jagody"))
        buttony.append(Button(POCZATEK_STEROWANIA_X, POCZATEK_STEROWANIA_Y + 16 * ODSTEP, self.__ekran, "Barszcz"))
        for button in buttony:
            button.draw()
        self.__narysuj_plansze(self.__swiat.get_organizmy(), 1)  # 1 to jest kontrolka, dzieki ktorej nie wyczyscimy ekranu
        return self.__interakcja_buttony(buttony)

# funckja sprawdza, ktory przycisk zostal nacisniety i zwraca jego wartosc
    def __interakcja_buttony(self, buttony):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(buttony)):
                        czy_przycisk = buttony[i].interakcja()
                        if czy_przycisk:
                            return i

    def __czy_dodac_organizm(self):
        x, y = pygame.mouse.get_pos()
        if x < self.__x * SZEROKOSC:
            if y < self.__y * SZEROKOSC:
                wspolrzednax = x // 20
                wspolrzednay = y // 20
                tmp = self.__swiat.organizm_punkt(Polozenie(wspolrzednax, wspolrzednay))
                if tmp is None:
                    nr_zwierze = self.__wyswietl_opcje_interakcja()
                    self.__swiat.dodaj_organizm(wspolrzednax, wspolrzednay, nr_zwierze)
                    self.__narysuj_plansze(self.__swiat.get_organizmy())


Gospodarz()
