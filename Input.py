import pygame


class Input(pygame.sprite.Sprite):

    def __init__(self, x, y, w, font, screen):
        super().__init__()
        self.__color = (0, 0, 0)
        self.__rect = pygame.Rect(x, y, w, 30)
        self.__font = font
        self.__screen = screen
        self.__text = ""
        self.__txt_surface = font.render("", True, self.__color)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return self.__text
                elif event.key == pygame.K_BACKSPACE:
                    self.__text = self.__text[:-1]
                else:
                    self.__text += event.unicode
        self.__txt_surface = self.__font.render(self.__text, True, self.__color)
        return 0

    def set_text(self, text):
        self.__text = text

    def draw(self):
        self.__screen.blit(self.__txt_surface, (self.__rect.x + 5, self.__rect.y + 5))
        pygame.draw.rect(self.__screen, self.__color, self.__rect, 2)
