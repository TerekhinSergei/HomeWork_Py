# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент
# с нулевым значением.
# Пример: - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random
num = int (input('Введите число: '))
numbers = []
for i in range(num):
    numbers.append(random.randint(-99,100))
print(f'исходный массив {numbers}')

i = 0 
for n in numbers:  
    i +=1
    if n < 0:  
        numbers.insert(i, 0)
print(f'новый массив -> {numbers}')


