import pygame

from check.const import RED, SQUARE_SIZE, GREY,CROWN

class Piece:
    PADDING = 15  # "Толщина" шашки
    OUTLINE = 2  # толщина границы

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):  # Функция вычисляет позицию шашки и ставит ее в середину квадрата путем деления на 2
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):  # Превращает шашку в дамку
        self.king = True

    def draw(self, win): # Отрисовываем шашку
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))  # Накладывает изображение короны

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):  # Возвращает цвет обьекта
        return str(self.color)
