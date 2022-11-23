# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число,
# и что это действительно входит в нужный диапазон
# Пример: 6 -> да    7 -> да   1 -> нет

num = int(input('введите число, определяющее день недели: '))

if num == 6 or num == 7:
    print('да')
else:
    if num < 1 or num > 7:
        print('в неделе 7 дней - введите цифру от 1 до 7')
    else:
        print('нет')
