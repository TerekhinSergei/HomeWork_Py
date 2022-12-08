# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета.
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random, time
from typing import Optional


def give_int_num(input_string: str,
                 min_num: Optional[int] = None,
                 max_num: Optional[int] = None) -> int:
    """
    Выпытывает у пользователя число в диапзоне от  min_num до  mах_num:

    Args:
    input_string - предложение ввода
    Returns:
    int - число
    """
    while True:
        try:
            num = int(input(input_string))
            if min_num and num < min_num:
                print(f'Введите больше {min_num-1}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше, чем {max_num+1}')
                continue
            return num
        except ValueError:
            print('Возможно это не число, попробуйте еще раз')


player1_name = input('Как Вас зовут? > ')
gam_t = give_int_num('выберите тип игры: 1 - с соперником, 0 - с ботом: > ', 0, 1)
if gam_t:
    game_type = True
    player2_name = input('Как зовут второго игрока? > ')
else:
    game_type = False
    player2_name = '"БОТ-любитель конфет"'

kucha = give_int_num('Введите количество конфет в куче: > ')
max_out = give_int_num('введите максимальное количество забираемых конфет: > ')
print(f'Итак:\n На столе лежит {kucha} конфет. Играют {player1_name} и {player2_name} делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем {max_out} конфет. Все конфеты достаются сделавшему последний ход.\n')
_ = input('ГОТОВЫ?')

print('а теперь жеребьевка!\n')
time.sleep(1)
num = (random.randint(0, 1))
if not num:
    print('начинает ', player1_name)
    player_start = True
else:
    print('начинает ', player2_name)
    player_start = False
time.sleep(1)

print(f'И так -> В куче {kucha} конфет')
while kucha > 0:
    if player_start:
        player_name = player1_name
    else:
        player_name = player2_name

    # if kucha <= max_out:
    #     max_out = kucha

    if game_type:
        out_pts = give_int_num(
            f'{player_name}, сколько конфет вы берете? > ', 1, max_out)
    elif player_start:
        out_pts = give_int_num(
            f'{player_name}, сколько конфет вы берете? > ', 1, max_out)
    else:
        out_pts = (random.randint(1, max_out))

    print(f'{player_name} забрал {out_pts} конфет')

    kucha -= out_pts

    if kucha <= 0:
        print(f'{player_name} забрал(а) последние конфеты - у нас есть победитель')
        print(f'Победил(а) {player_name}! Поздравляю!')
    else:
        print(f'В куче осталось {kucha} конфет')

    if player_name == player1_name:
        player_start = False
    else:
        player_start = True
