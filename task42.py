# 2 - Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

from typing import List

def get_unical_num(num: List[int]) -> List[int]:
    """
    Возвращает список уникальных элементов списка

    Args:
    numbers - список целых чисел
    Returns:
    list - список целых чисел
    """
    mul =[]
    for i in num:     
        if not mul.count(i):
                mul.append(i) 
        mul.sort()   
    return mul

pos = '1,1,1,7,5,3,3,5,1,2,2,3,3,4,5,7'
num = list(map(int,pos.split(',')))
result = get_unical_num(num) 
print(f'список уникальных элементов последовательности {num} -> {result}')