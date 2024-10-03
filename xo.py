import os
import random

clear = lambda: os.system('cls')
area = [['   ', '   ', '   '], ['   ', '   ', '   '], ['   ', '   ', '   ']]
labeled_cells = {11, 12, 13, 21, 22, 23, 31, 32, 33}

def draw_area():
    current_iteration = 0

    for i in area:
        draw_line = ''
        current_iteration += 1

        for j in i:
            draw_line = draw_line + j + '|'

        draw_line = draw_line[:-1]
        print(draw_line)

        if current_iteration != 3:
            print('---|---|---')
    print()

def cell_selection():
    is_correct_input = True

    while True:
        selected_cell = input(
            "Выберите клетку (пример ввода 12, где 1, это строка, а 2, это столбец):\n->"
            if is_correct_input else "Некорректный ввод, попробуйте ещё раз:\n->"
        )

        if selected_cell.isnumeric():
            selected_cell = int(selected_cell)
        else:
            is_correct_input = False
            continue

        n, m = selected_cell // 10, selected_cell % 10

        if (n > 0 and m > 0) and (n < 4 and m < 4):
            if area[n - 1][m - 1] != '   ':
                is_correct_input = False
            else:
                return n, m
        else:
            is_correct_input = False

def user_move(n, m):
    area[n - 1][m - 1] = ' x '
    labeled_cells.remove(n * 10 + m)

def bot_move():
    cell = random.choice(list(labeled_cells))
    area[cell // 10 - 1][cell % 10 - 1] = ' 0 '
    labeled_cells.remove(cell)

def determining_the_winner():
    who_winner = ' '

    for i in range(3):
        if len(set(area[i])) == 1:
            who_winner = area[i][0][1:2]
            return who_winner

        column = [area[0][i], area[1][i], area[2][i]]
        if len(set(column)) == 1:
            who_winner = column[0][1:2]
            return who_winner

    main_diagonal = [area[0][0], area[1][1], area[2][2]]
    if len(set(main_diagonal)) == 1:
        who_winner = main_diagonal[0][1:2]
        return who_winner

    secondary_diagonal = [area[0][2], area[1][1], area[2][0]]
    if len(set(secondary_diagonal)) == 1:
        who_winner = secondary_diagonal[0][1:2]
        return who_winner

    return who_winner


def start_game():
    is_not_game_over = True
    result = ''

    while is_not_game_over:
        #Ход игрока
        clear()
        draw_area()
        n, m = cell_selection()
        user_move(n, m)

        result = determining_the_winner()
        if result != ' ':
            is_not_game_over = False
            break

        #Ход бота
        clear()
        draw_area()
        bot_move()

        #Проверка победителя
        result = determining_the_winner()
        if result != ' ':
            is_not_game_over = False

    #clear()
    draw_area()
    print('Победили', result + '!')

start_game()


