# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 => x∈(0, ∞) u y∈(0,∞)
import sys

quarter_num = int (input('введите номер четверти: '))

if quarter_num < 1  or quarter_num > 4:
    sys.exit('число не соответсвует требуемому диапазону')  # нашел в интернете
    
if quarter_num == 1:
    print ('X∈(0,∞) и Y∈(0,∞)')
else:
    if quarter_num == 2:
        print ('X∈(0,-∞) и Y∈(0,∞)')
    else:
        if quarter_num == 3:
            print ('X∈(0,-∞) и Y∈(0,-∞)')
        else:
            print ('X∈(0,∞) и Y∈(0,-∞)')