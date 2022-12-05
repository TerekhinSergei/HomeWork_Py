# 1 - Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
def give_int_num(input_string: str ) -> int:
    """
    Запрашивает целое число

    Args:
    input_string - предложение ввода
    Returns:
    int - число
    """
    while True:
        try:
            num = int(input(input_string))            
            return num
        except ValueError:
            print('Неправильный ввод. Попробуйте еще раз')   
        

def get_multiplier_list(num: int) -> list:
    """
    Принимает целое число. Возвращает список простых множителей введенного числа
    
    Args:
        int - целое число
    Returns:
        list - список простых множителей введенного числа
    """     
    mult =[]
    for i in range(2,num+1):     
        while not num % i:
            if not mult.count(i):
                mult.append(i)
            num //= i            
            i = i            
        else:
            i += 1            
    return mult



num = give_int_num('Введите целое число: ')
multiplier = get_multiplier_list(num) 
print(f'Простые множители числа {num} -> {multiplier}')