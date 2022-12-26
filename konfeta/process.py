from random import randint

import game


def player_is_bot ():
    name_player = input('Введите свое имя: ')
    candies = 100
    max_move = 28
    count_check_win = candies // max_move
    moves = randint(0, 1)
    win = False
    while not win:
        if moves % 2 == 0:
            candies = game.move_human(name_player, candies, max_move)
        else:
            candies = game.move_bot(candies, max_move)
        if moves >= count_check_win - 1:
            temp = game.check_win(candies, moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        moves += 1

def player_is_human():
    name_first = input('Введите имя первого игрока: ')
    name_second = input('Введите имя второго игрока: ')
    candies = 100
    max_move = 28
    count_check_win = candies // max_move
    moves = randint(0, 1)
    win = False
    while not win:
        if moves % 2 == 0:
            candies = game.move_human(name_first, candies, max_move)
        else:
            candies = game.move_human(name_second, candies, max_move)
        if moves >= count_check_win - 1:
            temp = game.check_win(candies, moves, name_first, name_second)
            if temp:
                print(f'{temp} выиграл(а)')
                win = True
        moves += 1
        

# def player_is_bot ():
#     name_player = input('Введите свое имя: ')
#     candies = 100
#     max_move = 28
#     count_check_win = candies // max_move
#     moves = randint(0, 1)
#     win = False
#     while not win:
#         if moves % 2 == 0:
#             candies = game.move_human(name_player, candies, max_move)
#         else:
#             candies = game.move_bot(candies, max_move)
#         if moves >= count_check_win - 1:
#             temp = game.check_win(candies, moves, name_player, 'Бот')
#             if temp:
#                 print(f'{temp} выиграл')
#                 win = True
#         moves += 1