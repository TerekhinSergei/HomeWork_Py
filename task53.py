# Создайте программу для игры в ""Крестики-нолики"".
# Романом предложено игровое поле вида [['*','*','*'],['*','*','*'],['*','*','*']]

from typing import List

def draw_gamefield(game_field: List[str]):
    """
    Выводит в консоль игровое поле в виде три строки по три позиции
    Args:
    game_field: List[str] - List игрового поля с символами типа str
    """    
    for line in game_field:
        print(line)
    
def put_symbol(simbol: str):
    """
    Запрашивает у игрока позицию и устанавливает на игровое поле символ Х или О
    Args:
    simbol: str - символ Х или О
    """ 
    simbol_insert = False
    while not simbol_insert:        
        answer = input(f'Введите позицию игрового поля (две цифры через пробел) куда поставим {simbol}? > ').split(' ')
        answer_line = answer[0]
        answer_pos = answer[1]        
        try:
            answer_line = int(answer_line)
            answer_pos = int(answer_pos)
        except ValueError:
            print("Ошибка ввода. Вы уверены, что ввели два числа через пробел?")
            continue
        if 0 < answer_line <= 3 and 0 < answer_pos <= 3:
            line = game_field[answer_line - 1]            
            if line[answer_pos - 1] not in "XO":
                line[answer_pos - 1] = simbol                
                simbol_insert = True
            else:
                print("Клетка уже занята! введи другое значение.")
        else:
            print("Ошибка ввода. Вы уверены, что ввели два числа через пробел")


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
    win_line = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for line in game_field:
        for s in line:
            now_line.append(s) #перевод игрового поля в простой список (для 3 по 3 не нашел варианта проверки)
    for block in win_line:
        if now_line[block[0]] == now_line[block[1]] == now_line[block[2]]:
            return now_line[block[0]] 
    return False


game_field = [['1 1','1 2','1 3'],['2 1','2 2','2 3'],['3 1','3 2','3 3']]

draw_gamefield(game_field)

for counter in range(9):
 
    if counter % 2 == 0:
        put_symbol(" X ")
    else:
        put_symbol(" O ")

    draw_gamefield(game_field)

    simbol = check_win_line(game_field)
    
    if simbol:
        print(f'игрок cтавивший {simbol} выиграл!')
        break
    if counter == 8:
        print("Ничья!")
        break

print('Игра завершена.')        



