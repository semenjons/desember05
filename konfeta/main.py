
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import os
import process

os.system('cls')

tgame = input('Введите 1, для начала игры или любую другую цифру, если хотите играть с ботом ')
if (tgame == '1'):
    process.player_is_human()
else:
    intel = input()   
    process.player_is_bot ()