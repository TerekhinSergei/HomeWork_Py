# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

def get_numbers_list(input_list: str ) -> list:
    """
    Просит пользователя ввести ряд чисел через пробел, возвращает список вещественых чисел

    Args:
        input_string - предложение ввода
    Returns:
        list - список введенных чисел 
    """  
    numbers = []
    numbs = (input(input_list).split(' '))
    for i in numbs:
        numbers.append(float(i))
    return numbers
    
def get_part_after_point(numbers: list) -> list: 
    """
    Принимает список вещественых чисел, возвращает список дробных частей чисел в виде 0.xyz

    Args:
        list - исходный список
    Returns:
        list - преобразованный список
    """              
    for n in numbers:        
        parts_list.append(round(float(n)-int(n),10))
    return parts_list

#numbers = [4.07, 5.1, 8.2444, 6.9814]
numbers = get_numbers_list('введите несколько вещественных чисел через пробел: ')[:]
parts_list = []

get_part_after_point(numbers)

print(f'исходный массив {numbers}')
print(f'разница между max и min значением дробной части элементов -> {round(max(parts_list)- min(parts_list), 10)} ')
print(f"другое представление разницы -> {((str(round(max(parts_list)- min(parts_list), 10))).split('.')[1])} ")

