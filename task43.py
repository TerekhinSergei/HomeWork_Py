# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем 
# регистре тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

from typing import List

def change_spisok(spisok: List[str], accept: str) -> str:
    """
    Принимает список. Возвращает измененый список в виде строки, в котором большими буквами выделены ФИО имеющие 5 баллов

    Args:
    spisok - исходный список,  accept - признак для внесения изменений (5)
    Returns:
    str - строка с измененными данными
    """    
    file_spisok = ''
    for name in spisok:
        if name.count(accept):
            name = name.upper() 
        string = name + '\n'                              
        file_spisok += string
    return file_spisok    

file_spisok = open('vedomost.txt', 'r', encoding='utf-8') 
lines_spisok = file_spisok.read().split('\n')  ## читаем из файла
file_spisok.close()

spisok_new = change_spisok(lines_spisok, accept='5') ## меняем текст в файле

## перезапись в исходный файл 'vedomost.txt'
file_spisok = open('vedomost.txt', 'w', encoding='utf-8') 
file_spisok.write(spisok_new)
file_spisok.close()

## запись в новый файл 'vedomost_new.txt'
# spisok_new=change_spisok(lines_spisok, accept='5')
# file_spisok_new = open('vedomost_new.txt', 'w', encoding='utf-8') 
# file_spisok_new.write(spisok_new)
# file_spisok_new.close

## вывод в консоль изменений записанных в файл
# file_spisok_new = open('vedomost.txt', 'r', encoding='utf-8') 
# file_spisok_new = open('vedomost_new.txt', 'r', encoding='utf-8') 
# lines_spisok_new = file_spisok_new.read()
# print(f'новый список: \n{lines_spisok_new}')
# file_spisok_new.close