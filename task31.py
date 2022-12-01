# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
def create_list(numbers):    
    for i in range(int(input('Введите количество элементов списка: '))):
        numbers.append(random.randint(1,9))
    return numbers   


def get_sum_odd_elements(numbers: list) -> int:
    """
    Возвращает сумму элементов списка, стоящих на нечётной позиции
    
    Args:
        list - список чисел
    Returns:
        int - число
    """  
    summa = 0
    i = 0 
    for n in numbers:      
        if i%2:  
            summa += n        
        i +=1
    return summa    

numbers = []
print(f'исходный список {create_list(numbers)}')   
print(f'сумма элементов на нечетных позициях = {get_sum_odd_elements(numbers)}')