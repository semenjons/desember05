
from random import randint

def move_human(name_player, candies, max_move):
    valid = False
    while not valid:
        move = input(f'{name_player}, Ваш ход ')
        try:
            move = int(move)
            if move > 0 and move <= max_move and move <= candies:
                print(f'Вы забрали {move} конфет')
                candies -= move
                print(f'Осталось {candies} конфет')
                valid = True
            else:
                print(f'Количество взятых конфет должно быть в интервале от 1 до {max_move} или не больше остатка')
        except:
            print('Необходимо ввести целое число ЕКАРНЫЙ БАБАЙ!!!!')
    return candies


def move_bot(candies, max_move):
    move = candies % (max_move + 1)
    if move == 0:
        move = randint(1, max_move) if candies >= max_move  else candies
    print(f'Бот забрал {move} конфет')
    candies -= move
    print(f'Осталось {candies} конфет')
    return candies

def check_win(candies, moves, first_name, second_name):
    if candies == 0:
        return first_name if moves % 2 == 0 else second_name
    else:
        return False