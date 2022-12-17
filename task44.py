# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное 
# количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

from functions import give_int_num

def get_encript_text(alfabet: str, text: str, key: int) -> str:
    """
    Принимает строку. Возвращает зашифрованную строку

    Args:
    alfabet - алфавит участвующий в шифровани,  text - строка подлежащая шифрованию , key - ключ шифрования(величина смещения)
    Returns:
    str - зашифрованная строка
    """       
    en_text = ''
    alfabet_long = len(alfabet)
    for simbol in text: 
        i = 0               
        #index =alfabet.find(simbol)
        for s in alfabet:
            index =alfabet.find(simbol)
            if simbol == s:
                index = i + key
            i +=1
        if index > alfabet_long:
            index -= alfabet_long
        #index = (index+key)%alfabet_long
        en_text += alfabet[index]
    return en_text

def get_decript_text(alfabet: str, text: str, key: int) -> str:
    """
    Принимает зашифрованную строку. Возвращает расшифрованную строку

    Args:
    alfabet - алфавит участвующий в шифровани,  text - строка подлежащая дешифрованию , key - ключ шифрования(величина смещения)
    Returns:
    str - расшифрованная строка
    """     
    de_text = ''
    alfabet_long = len(alfabet)    
    for simbol in text: 
        i = 0               
        for s in alfabet:
            if simbol == s:
                index = i - key
            i +=1
        if index < 0:
            index = alfabet_long + index 
        if index >= alfabet_long:
            index = index - alfabet_long         
        de_text += alfabet[index]
    return de_text
    

alfabet ='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя !"#$%&'+"'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
initial_text = 'Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево. Сдвиг часто называют ключом шифрования. Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.'
key = 5

# file_initial = open('initial.txt', 'r', encoding='utf-8') ## если исходный текст в файле
# initial_text = file_initial.read()
# file_initial.close

en_text = get_encript_text(alfabet, initial_text, key) ## шифруем текст
file_encript = open('encript.txt', 'w', encoding='utf-8') 
file_encript.write(en_text) ## записываем зашифрованный файл
file_encript.close()

print('текст зашифрован см. file "encript.txt"') 
key = give_int_num('Введите ключ дешифрования (вправо положительной число, влево - отрицательное)\nПОСКАЗКА - введите "5": ')

file_encript = open('encript.txt', 'r', encoding='utf-8') 
enс_text = file_encript.read() ## читаем зашифрованный файл
file_encript.close()

de_text = get_decript_text(alfabet, enс_text, key) ## расшифровываем текст

file_decript = open('decript.txt', 'w', encoding='utf-8') 
file_decript.write(de_text) ## записываем расшифрованный файл
file_decript.close()

print('файл расшифрован см. file "decript.txt"')