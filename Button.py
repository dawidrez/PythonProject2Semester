import pygame
WYSOKOSC = 20
SZEROKOSC = 100
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)


class Button:

    def __init__(self, punkt_x, punkt_y, screen, napis, wysokosc=WYSOKOSC, szerokosc=SZEROKOSC, kolor_tla=BIALY, kolor_napisu=CZARNY):
        self.__wysokosc = wysokosc
        self.__czcionka = pygame.font.Font("freesansbold.ttf", 15)
        self.__szerokosc = szerokosc
        self.__kolor_tla = kolor_tla
        self.__kolor_napisu = kolor_napisu
        self.__punkt_x = punkt_x
        self.__punkt_y = punkt_y
        self.__screen = screen
        self.__button = pygame.Rect(punkt_x, punkt_y, self.__szerokosc, self.__wysokosc)
        self.__napis = napis

    def draw(self):
        pygame.draw.rect(self.__screen, self.__kolor_tla, self.__button)
        text_surf = self.__czcionka.render(self.__napis, True, self.__kolor_napisu)
        self.__screen.blit(text_surf, (self.__punkt_x + 2, self.__punkt_y + 2))  # +2 pixele zeby odstep od scianek

    def interakcja(self):
        czy_przycisk = self.__button.collidepoint(pygame.mouse.get_pos())
        return czy_przycisk
