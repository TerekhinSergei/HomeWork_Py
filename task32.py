# 2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: 
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
import math

def create_list(numbers: list) -> list:
    """
    Спрашивает количество элементов и возвращает список, стоящий из случайных целых чисел
    
    Args:
        list - пустой список
    Returns:
        list - список целых чисел
    """      
    for i in range(int(input('Введите количество элементов списка: '))):
        numbers.append(random.randint(1,9))
    return numbers   

def get_list_product_pairs_elements(numbers: list) -> list:
    """
    Возвращает список, стоящий из произведения пар принятого списка
    
    Args:
        list - список чисел
    Returns:
        list - список произведения пар
    """  
    product_list = []
    for i in range(math.ceil(len(numbers)/2)):
        product_list.append(numbers[i]*numbers[-(i+1)])
    return product_list   

numbers = []
print(f'исходный список {create_list(numbers)}')  
print(f'произведение пар элементов = {get_list_product_pairs_elements(numbers)}')

