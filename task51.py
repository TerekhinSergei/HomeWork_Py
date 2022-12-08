# Напишите программу, удаляющую из текста все слова, содержащие заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок


def read_data_string(filename: str, coding:  str) -> str:
    """
    Возвращает текст из файла в виде строки

    Args:
    filename: str - Имя читаемого файла, coding: str - кодировка файла
    Returns:
    str - данные из файлв в виде строки
    """
    with open(filename, 'r', encoding=coding) as file:
        data = file.read()
    return data


def add_string_to_file(filename: str, coding:  str, string: str):
    """
    Дописывает текст в файла

    Args:
    filename: str - Имя  файла, coding: str - кодировка файла
    string: str - строка которую надо записать в файл
    """
    with open(filename, 'a', encoding=coding) as file:
        file.write(string)

# чтение текста из фала
my_text = read_data_string('povtor.txt', 'utf-8')

print(f'исходный текст:\n{my_text}')

param_delet = input('введите параметр для удаления: ')
new_text = list(filter(lambda s: s.find(param_delet) == -1, my_text.split(' ')))
new_text = " ".join(new_text)

# добавление модифицированного текста к файлу
add_string_to_file('povtor.txt', 'utf-8',
                   f'\nв тескте удалены все слова содержащие "{param_delet}":\n\n' + new_text)

# вывод модифицированного текста в консоль
print(f'\nв тескте удалены все слова содержащие "{param_delet}":\n{new_text}')
