# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from functions import create_list, List

def get_sum_odd_elements(numbers: List[int]) -> int:
    """
    Возвращает сумму элементов списка, стоящих на нечётной позиции
    
    Args:
        list - список чисел
    Returns:
        int - число
    """  
    summa = 0   
    for n in range(1, len(numbers),2):      
        summa += n                
    return summa    

numbers = create_list()
print(f'исходный список {numbers}')   
print(f'сумма элементов на нечетных позициях = {get_sum_odd_elements(numbers)}')