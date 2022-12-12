# 2-Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

import math, random
from functions import give_int_num

numbers = [random.randint(0, 10) for _ in range(give_int_num('Введите количество элементов списка: '))]
print(f'исходный список -> {numbers}')
product_list = list(map(lambda i: (numbers[i]*numbers[-(i+1)]), [i for i in range(math.ceil(len(numbers)/2))]))
print(f'произведение пар элементов -> {product_list}')
