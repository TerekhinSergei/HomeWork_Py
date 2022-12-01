# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример: 45 -> 101101  3 -> 11    2 -> 10

# с использованием рекурсии
def convert_binary(num: int) -> list: 
    """
    Принимает число которое требуется перевестив двоичную систему, возвращает список разрядов двоичного числа

    Args:
        int - число которое требуется перевестив двоичную систему
    Returns:
        list - список разрядов двоичного числа
    """    
    if not num:
        binar.reverse()
        return binar
    binar.append(num % 2)
    convert_binary(num // 2) 
    
num = int(input('введите число: '))
binar = []
convert_binary(num)
print(f'число {num} в двоичной системе -> ', end='')
for i in binar:
    print(i, end='')
#print("".join(map(str,binar)))

# num = int(input('введите число: '))
# n = num
# binar = []
# while num > 0:
#     binar.append(int(num%2))
#     num //= 2
# binar.reverse()

# print(f'число {n} в двоичной системе -> ', end='')
# for i in binar:
#     print(i, end='')