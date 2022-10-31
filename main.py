import pygame
from check.const import WIDTH, HEIGHT, SQUARE_SIZE
from board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # создаем окно с заданными размерами
pygame.display.set_caption('Шашки')  # заголовок для окна

FPS = 60

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():  # главная функция
    run = True  # флаг для выполнения цикла
    clock = pygame.time.Clock()
    board = Board()  # создаем объект класса



    while run:
        clock.tick(FPS)

        for event in pygame.event.get():  # функция ожидания события
            if event.type == pygame.QUIT:  # если событие Выход - завершаем игру командой pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # обработка события при нажатой кнопки мыши
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(WIN)  # рисуем поля доски
        pygame.display.update()  # обновляем окно

    pygame.quit()

main()
