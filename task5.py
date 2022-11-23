# 5- Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5.09
# A (7,-5); B (1,-1) -> 7.21
import math

coordinates =  input('введите координаты точка А через пробел: ').split(' ')
x_a = float (coordinates[0])  
y_a = float (coordinates[1]) 
coordinates =  input('введите координаты точка B через пробел: ').split(' ')
x_b = float (coordinates[0])  
y_b = float (coordinates[1]) 

result = math.sqrt(((x_a - x_b)**2) + ((y_a - y_b)**2))

print (f'длина отрезка А({x_a}, {y_a}) B({x_b}, {y_b}) = {round(result, 2)}')

