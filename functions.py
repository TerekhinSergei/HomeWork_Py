import random
from typing import List

def create_list(numbs =[]):    
    for i in range(int(input('Введите количество элементов списка: '))):
        numbs.append(random.randint(1,9))
    return numbs  


def give_int_num(input_string: str ) -> int:
    """
    Запрашивает целое число

    Args:
    input_string - предложение ввода
    Returns:
    int - число
    """
    while True:
        try:
            num = int(input(input_string))            
            return num
        except ValueError:
            print('Неправильный ввод. Попробуйте еще раз')       