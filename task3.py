# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
import sys

num_x = int(input('введите координату Х не равную 0: '))
num_y = int(input('введите координату Y не равную 0: '))

if num_x == 0 or num_y == 0:
    sys.exit('введите координату отличную от 0 !')   # нашел в интернете

if num_x > 0:
    if num_y > 0:
        print('quarter = 1')
    else:
        print('quarter = 4')
else:
    if num_y > 0:
        print('quarter = 2')
    else:
        print('quarter = 3')
