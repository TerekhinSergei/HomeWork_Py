# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension

import random

#numbers = [0, 2, 2, 3, 3, 5, 5, 7, 7, 10, 10, 9, 11, 12, 13, 15]
numbers = [random.randint(1, 100) for _ in range(200)]
print(f'список без совпадений -> {list(filter(lambda x: x[0] != x[1], enumerate(numbers)))}')
print(f'список удаленных -> {list(filter(lambda x: x[0] == x[1], enumerate(numbers)))}')   


### при необходимости перенумеровать оставшиеся кортежи по порядку
# product = list(filter(lambda x: x[0] != x[1], enumerate(numbers)))
# count, numbers = zip(*product) 
# print(f'результирующий список -> {list(enumerate(numbers))}') 

