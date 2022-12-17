# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
# Первая функция - текст зашифровывает
# Вторая - расшифровывает

from typing import List


def get_rle_encode(string_for_encoding:str) -> str:
    """
    Принимает строку для RLE кодирования. Возвращает сжатую cтроку. АЛГОРИТМ МОДИФИЦИРОВАН - если символ не повторяется, возвращается просто символ(без 1)

    Args:
    string_for_encoding - исходная строка
    Returns:
    str - сжатая строка 
    """   
    encode = ''
    i = 0
    while i < len(string_for_encoding):        
        count = 1
        while i + 1 < len(string_for_encoding) and string_for_encoding[i] == string_for_encoding[i + 1]:
            count = count + 1
            i = i + 1        
        if count == 1: # Если символ не повторяется (только 1), то убираем единицу,
            count = '' # чтобы сответсвовать образцу и сократить длину кодированой записи 
        encode += str(count) + string_for_encoding[i]
        i = i + 1
    return encode

def get_rle_decode(string_for_decoding:str) -> str: 
    """
    Принимает закодированную строку для RLE декодирования. Возвращает декодированную строку

    Args:
    string_for_decoding - закодированная RLE строка 
    Returns:
    str - декодированная строка 
    """          
    decode = '' 
    count = '' 
    for simbol in string_for_decoding:          
        if simbol.isdigit(): 
            count += simbol 
        elif not simbol.isdigit() and count == '': #Если у символа нет предшествующего числа,
            decode += simbol                       #сразу добавляем его к декодированной строке
        else:        
            decode += simbol * int(count)
            count = ''     
    return decode

## читаем из файл исходный текст
file_initial = open('initial_rle.txt', 'r', encoding='utf-8') 
initial_text = file_initial.read()
file_initial.close()

#print('исходный текст:\n', initial_text)

cod_text = get_rle_encode(initial_text) ## кодируем текст(сжимаем)

file_encode = open('encode.txt', 'w', encoding='utf-8') 
file_encode.write(cod_text) ## записываем в файл закодированный (сжатый) текст
file_encode.close()

print('закодированный (сжатый) текст: ', cod_text)

file_encode = open('encode.txt', 'r', encoding='utf-8') 
text = file_encode.read()  ## читаем из файла закодированный (сжатый) текст
file_encode.close()

decod_text = get_rle_decode(text) ## декодируем текст (восстанавливаем)

print('\nраскодированный текст:\n', decod_text)

## если надо записать в файл раскодированный текст
# file_decode = open('decode.txt', 'w', encoding='utf-8') 
# file_decode.write(decod_text)
# file_decode.close

# print('encoding_text ', cod_text)


def read_data_list(filename: str ) -> List[str]:

    with open(filename, 'r') as file:
        data = file.read().rstrip().split('\n')
    return data

def write_data_list(filename: str , string: str ) -> List[str]:

    with open(filename, 'w') as file:
        data = file.write(string)

