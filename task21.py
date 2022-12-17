# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 67.82 -> 23
# - (-0.56) -> 11

num = input('Введите число: ')
sum = 0
for i in num:    
    if i.isdigit():
        sum += int(i)           

print(sum)

##############
float_num = float(input('Введите вещественное число: '))
float_num = abs(float_num)  # убирается минус
while float_num != int(float_num):
    float_num = round(float_num*10, 10)
sum_digits = 0
while float_num > 0:
    sum_digits += float_num % 10
    float_num //= 10
print(sum_digits)

