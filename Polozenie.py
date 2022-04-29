class Polozenie:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        x = self.__x
        y = self.__y
        return "(" + str(x) + "," + str(y) + ")"

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def przesuniecie(self, x, y):  # x,y to wymiary swiata
        pola = []
        x1 = self.__x
        y1 = self.__y
        if x1 - 1 >= 0:
            pola.append(Polozenie(x1-1, y1))
        if y1 - 1 >= 0:
            pola.append(Polozenie(x1, y1 - 1))
        if x1 + 1 < x:
            pola.append(Polozenie(x1 + 1, y1))
        if y1 + 1 < y:
            pola.append(Polozenie(x1, y1+1))
        return pola

    # pola dla dzieci dla roslinki
    def get_pola_dla_dzieci_roslina(self, x, y):
        pola = []
        x1 = self.__x
        y1 = self.__y
        if x1 > 0:
            pola.append(Polozenie(x1 - 1, y1))
            if y1 > 0:
                pola.append(Polozenie(x1 - 1, y1 - 1))
            if y1+1 < y:
                pola.append(Polozenie(x1 - 1, y1 + 1))
        if x1+1 < x:
            pola.append(Polozenie(x1 + 1, y1))
            if y1 > 0:
                pola.append(Polozenie(x1 + 1, y1 - 1))
            if y1+1 < y:
                pola.append(Polozenie(x1 + 1, y1 + 1))
        if y1 > 0:
            pola.append(Polozenie(x1, y1 - 1))
        if y1+1 < y:
            pola.append(Polozenie(x1, y1 + 1))
        return pola

    # pola  dla dieci  dla zwierzecia
    def get_pola_dla_dzieci_zwierze(self, partner, x, y):
        pola = []
        x1 = self.__x
        x2 = partner.get_polozenie().get_x()
        y1 = self.__y
        y2 = partner.get_polozenie().get_y()
        if x1 == x2:
            if x1 > 0:
                pola.append(Polozenie(x1 - 1, y1))
                pola.append(Polozenie(x1 - 1, y2))
            if x1 + 1 < x:
                pola.append(Polozenie(x1 + 1, y1))
                pola.append(Polozenie(x1 + 1, y2))
            if y1 > 0 and y2 > 0:
                if y1 > y:
                    pola.append(Polozenie(x1, y2 - 1))
                else:
                    pola.append(Polozenie(x1, y1 - 1))
            if y1+1 < y and y2+1 < y:
                if y1 > y2:
                    pola.append(Polozenie(x1, y1 + 1))
                else:
                    pola.append(Polozenie(x1, y2 + 1))
        else:
            if y1 > 0:
                pola.append(Polozenie(x1, y1 - 1))
                pola.append(Polozenie(x2, y2 - 1))
            if y1 + 1 < y:
                pola.append(Polozenie(x1, y1 + 1))
                pola.append(Polozenie(x1, y2 + 1))

            if x1 > 0 and x2 > 0:
                if x1 > x2:
                    pola.append(Polozenie(x2 - 1, y2))
                else:
                    pola.append(Polozenie(x1 - 1, y1))
            if x1+1 < x and x2+1 < x:
                if x1 > x2:
                    pola.append(Polozenie(x1 + 1, y1))
                else:
                    pola.append(Polozenie(x2 + 1, y1))
        return pola
