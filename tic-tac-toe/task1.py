from typing import List
from colorama import Fore, Back, Style
from typing import List, Optional


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
                print(f'Введите больше {min_num}')
                continue
            if max_num and num > max_num:
                print(f'Введите меньше {max_num+1}')
                continue
            return num
        except ValueError:
            print('Похоже это не число, попробуте еще раз')


def draw_gamefield(game_field: List[str]):
    """
    Выводит в консоль игровое поле в виде три строки по три позиции
    Args:
    game_field: List[str] - List игрового поля с символами типа str
    """
    for line in game_field:
        print(line)
    print()


def put_symbol(simbol: str):
    """
    Запрашивает у игрока позицию и устанавливает на игровое поле символ Х или О
    Args:
    simbol: str - символ Х или О
    """
    simbol_insert = False
    while not simbol_insert:
        if simbol == " O ":
            cvet = Fore.BLUE
        else:
            cvet = Fore.RED

        print(cvet + f'куда поставим {simbol}')
        answer_line = give_int_num(
            'введите номер строки  > ', min_num=1, max_num=3)
        answer_pos = give_int_num(
            'введите номер столбца > ', min_num=1, max_num=3)
        print(Style.RESET_ALL)

        line = game_field[answer_line - 1]

        if line[answer_pos - 1] in ' X O ':
            print(
                Fore.RED + 'Клетка уже занята! введи другое значение.' + Style.RESET_ALL)
        else:
            line[answer_pos - 1] = simbol
            simbol_insert = True


def check_win_line(game_field: List[str]) -> bool or str:
    """
    Выполняет проверку наличия выгрышной комбинации на игровом поле
    Args:
    game_field: List[str] - List игрового поля с символами Х и O
    Returns:
    bool - есть ли выгрышная комбинация на игровом поле
    str - символ победитель    
    """
    now_line = []
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for line in game_field:
        for s in line:
            # перевод игрового поля в простой список (для 3 по 3 не нашел варианта проверки)
            now_line.append(s)
    for block in win_line:
        if now_line[block[0]] == now_line[block[1]] == now_line[block[2]]:
            return now_line[block[0]]
    return False


game_field = [['1 1', '1 2', '1 3'], [
    '2 1', '2 2', '2 3'], ['3 1', '3 2', '3 3']]
print(Back.WHITE)
print(Fore.BLACK + 'Привет, начинаем игру в крестики нолики\n' + Style.RESET_ALL)
draw_gamefield(game_field)

for counter in range(9):

    if counter % 2 == 0:
        put_symbol(" X ")
    else:
        put_symbol(" O ")

    draw_gamefield(game_field)

    simbol = check_win_line(game_field)

    if simbol:
        if simbol == " O ":
            cvet = Fore.BLUE
        else:
            cvet = Fore.RED
        print(cvet + f'игрок cтавивший {simbol} выиграл!\n' + Style.RESET_ALL)
        break
    if counter == 8:
        print(Back.GREEN + 'Ничья!\n' + Style.RESET_ALL)
        break

print(Back.YELLOW + Fore.BLACK + 'Игра завершена.' + Style.RESET_ALL)
